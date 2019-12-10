import re
import math, itertools

ENTROPY_THRESHOLD = .45

def get_token_pairs(characters):
    """Returns the mapping of each individual character to the next in the list
    """
    a, b = itertools.tee(characters)
    next(b, None)
    return zip(a, b)

def entropy(s):
	"""Returns the entropy of the string s
	"""
	e = 0
	for a, b in get_token_pairs(list(s)):
		if not ((str.islower(a) and str.islower(b)) or (str.isupper(a) and\
			str.isupper(b)) or (str.isdigit(a) and str.isdigit(b))):
			e += 1
	return float(e) / len(s)

# matches emails
def match_email(line):
    #https://emailregex.com/
    email = re.compile(r'([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)')
    output = re.findall(email,line)  
    if(len(output) > 0):
        return True
    return False

# matches Bitcoin private key, URI, extended public key
def match_bitcoin(line): 
    bitcoinAddress = re.compile(r'[13][a-km-zA-HJ-NP-Z1-9]{25,34}')
    bitcoinURI = re.compile(r'bitcoin:([13][a-km-zA-HJ-NP-Z1-9]{25,34})')
    bitcoinExtendedPublicKey = re.compile(r'(xpub[a-km-zA-HJ-NP-Z1-9]{100,108})(\\?c=\\d*&h=bip\\d{2,3})?')
    bitcoinPrivateKey = re.compile(r'[5KL][1-9A-HJ-NP-Za-km-z]{50,51}')

    regexes = [bitcoinAddress,bitcoinPrivateKey, bitcoinURI, bitcoinExtendedPublicKey]
    
    output = []
    for regex in regexes:
        matches = re.findall(regex,line)
        for m in matches:
            if entropy(m) >= ENTROPY_THRESHOLD:
                output.append(m)
    if(len(output) > 0):
        return True
    return False

# matches cryptokeys
def match_crypto(line):
    # keys in hex
    # 56-64 bit keys (DES)
    hex64bit = re.compile(r'[a-fA-F0-9]{14,16}')
    # 128, 192, 256 bit keys with extra parity bits (AES)
    hex128Bit = re.compile(r'[a-fA-F0-9]{32,36}') 
    hex192Bit = re.compile(r'[a-fA-F0-9]{48,54}')
    hex256Bit = re.compile(r'[a-fA-F0-9]{64,72}')
    # 2048 bit key (RSA)
    hex2048Bit = re.compile(r'[a-fA-F0-9]{512}')

    #keys in base64
    base64 = re.compile(r'^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=|[A-Za-z0-9+/]{4})(?:=[A-Za-z0-9+/]{4})?$')

    regexes = [hex64bit, hex128Bit, hex192Bit, hex256Bit, hex2048Bit, base64]

    output = []
    for regex in regexes:
        matches = re.findall(regex,line)
        for m in matches:
            if entropy(m) >= ENTROPY_THRESHOLD:
                output.append(m)
    if(len(output) > 0):
        return True
    return False

# matches passwords
def match_password(line):
    # password with at least 8 characters, one uppercase, one lowercase, one number and one special character
    #pw1 = re.compile(r'(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[#?!@$%^&*-])[A-Za-z\d#?!@$%^&*-]{8,}')
    # password with variable name 'password', 'pw', or 'p'
    pw2 = re.compile(r'(?:password|pw)(?: ?= ?)["|\']?[A-Za-z\d#?!@$%^&*-]+["|\']?')

    regexes = [pw2]

    output = []
    for regex in regexes:
        output.extend(re.findall(regex,line))
    if(len(output) > 0):
        return True
    return False

#matches API keys
def match_api_key(line):
    #https://gist.github.com/hsuh/88360eeadb0e8f7136c37fd46a62ee10
    AWSaccessKeyID = re.compile(r'(?<![A-Z0-9])[A-Z0-9]{20}(?![A-Z0-9])')
    AWSsecretAccessKey = re.compile(r'(?<![A-Za-z0-9/+=])[A-Za-z0-9/+=]{40}(?![A-Za-z0-9/+=])')
    AWSsecretAccessKeyAlternative = re.compile(r'[0-9a-zA-Z/+]{40}')
    #https://people.eecs.berkeley.edu/~rohanpadhye/files/key_leaks-msr15.pdf
    #Bitly
    BITsecretAccessKey = re.compile(r'R_[0-9a-f]{32,}')
    #Facebook
    FBsecretAccessKey = re.compile(r'[0-9a-f]{32,}')

    #FLICKR
    FLsecretAccessKey = re.compile(r'[0-9a-f]{16,}')

    #Foursquare
    FSsecretAccessKey = re.compile(r'[0-9A-Z]{48,}')

    #LinkedIn
    LIsecretAccessKey = re.compile(r'[0-9a-zA-Z]{16,}')

    #Twitter
    TWsecretAccessKey = re.compile(r'[0-9a-zA-Z]{35,44}')

    #only letter
    onlyLetters = re.compile(r'^[a-zA-Z]+$')
    regexar = [AWSsecretAccessKey,BITsecretAccessKey,FLsecretAccessKey,AWSsecretAccessKeyAlternative,TWsecretAccessKey,LIsecretAccessKey,FSsecretAccessKey, AWSaccessKeyID]

    output = []
    for regex in regexar:
        matches = re.findall(regex,line)
        for m in matches:
            if entropy(m) >= ENTROPY_THRESHOLD:
                output.append(m)
        # output.extend(re.findall(regex,line))
    if(len(output) > 0):
        return True
    return False

if __name__ == '__main__':
    pass
