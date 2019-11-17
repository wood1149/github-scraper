import re


#---BEGIN RSA PRIVATE KEY--- 

#matches API keys
def main(filePath):
    #https://gist.github.com/hsuh/88360eeadb0e8f7136c37fd46a62ee10
    AWSaccessKeyID = re.compile(r'(?<![A-Z0-9])[A-Z0-9]{20}(?![A-Z0-9])')
    AWSsecretAccessKey = re.compile(r'(?<![A-Za-z0-9/+=])[A-Za-z0-9/+=]{40}(?![A-Za-z0-9/+=])')

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

    regexar = [AWSaccessKeyID,AWSsecretAccessKey,BITaccessKeyID,BITsecretAccessKey,FBaccessKeyID,FLsecretAccessKey]
    outputar= []
    with open(filePath, 'r') as fd:
        text = fd.read()
        
        for exp in regexar:
            output = re.findall(exp,text)
            if(len(output) > 0):
                outputar.extend(output)
                
        if(len(outputar) > 0):
            print("Api key found " + filePath)
            print(outputar)
            return True
        return False

        
        
