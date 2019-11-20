import re


#---BEGIN RSA PRIVATE KEY--- 

# matches emails
def match_email(line):
    #https://emailregex.com/
    email = re.compile(r'([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)')
    output = re.findall(email,line)  
    if(len(output) > 0):
        print("Email found")
        print(output)
        return True
    return False

# matches Bitcoin address, URI, extended public key
def match_bitcoin(line): 
    bitcoinAddress = re.compile(r'[13][a-km-zA-HJ-NP-Z1-9]{25,34}')
    bitcoinURI = re.compile(r'bitcoin:([13][a-km-zA-HJ-NP-Z1-9]{25,34})')
    bitcoinExtendedPublicKey = re.compile(r'(xpub[a-km-zA-HJ-NP-Z1-9]{100,108})(\\?c=\\d*&h=bip\\d{2,3})?')

    regexes = [bitcoinAddress, bitcoinURI, bitcoinExtendedPublicKey]
    
    for regex in regexes:
        output = re.findall(regex,line)  
    if(len(output) > 0):
        print("Bitcoin info found")
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

    for regex in regexes:
        output = re.findall(regex,line)  
    if(len(output) > 0):
        print("Crypto key info found")
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
    BITaccessKeyID = re.compile(r'[0-9a-zA-Z_]{5,31}')
    BITsecretAccessKey = re.compile(r'R_[0-9a-f]{32}')
    #Facebook
    FBaccessKeyID = re.compile(r'[0-9]{13,17}')
    FBsecretAccessKey = re.compile(r'[0-9a-f]{32}')

    #FLICKR
    FLaccessKeyID = re.compile(r'[0-9a-f]{32}')
    FLsecretAccessKey = re.compile(r'[0-9a-f]{16}')

    #Foursquare
    FSaccessKeyID = re.compile(r'[0-9A-Z]{48}')
    FSsecretAccessKey = re.compile(r'[0-9A-Z]{48}')

    #LinkedIn
    LIaccessKeyID = re.compile(r'[0-9a-z]{12}')
    LIsecretAccessKey = re.compile(r'[0-9a-zA-Z]{16}')

    #Twitter
    TWaccessKeyID = re.compile(r'[0-9a-zA-Z]{18,25}')
    TWsecretAccessKey = re.compile(r'[0-9a-zA-Z]{35,44}')

    regexar = [AWSaccessKeyID,AWSsecretAccessKey,BITaccessKeyID,BITsecretAccessKey,FBaccessKeyID,FLsecretAccessKey,AWSsecretAccessKeyAlternative]
    
    for exp in regexar:
        output = re.findall(exp,line)  
    if(len(output) > 0):
        print("Api key found")
        return True
    return False

if __name__ == '__main__':
    pass
    