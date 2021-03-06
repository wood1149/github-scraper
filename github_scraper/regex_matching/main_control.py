from .regex_matching_strings import match_api_key as MatchAPI
from .regex_matching_strings import match_password as MatchPW
from .regex_matching_strings import match_crypto as MatchCrypto
from .regex_matching_strings import match_bitcoin as MatchBitcion 
from .regex_matching_strings import match_email as MatchEmail

gfilestr = ""
#takes in a map, runs regex matching on text, and returns type/line number of match
def main(fileMap, entropy=0.45):
    outputMap = {}
    for key in fileMap:
        outputMap[key] = []
        findMatches(key,fileMap[key],outputMap, entropy)
        
    return outputMap


def getLine(filestr=gfilestr):
    prevnl = -1
    while True:
      nextnl = filestr.find('\n', prevnl + 1)
      if nextnl < 0: break
      yield filestr[prevnl + 1:nextnl]
      prevnl = nextnl

def findMatches(key,fileString,outputMap,entropy=0.45):
    idx = 1
    for line in fileString.splitlines():
      if(MatchAPI(line,entropy)):
        if(len(outputMap[key]) == 0):
          outputMap[key] = ["API:" + str(idx)]
        else:
          outputMap[key].append("API:" + str(idx))

      if(MatchPW(line)):
        if(len(outputMap[key]) == 0):
          outputMap[key] = ["Password:" + str(idx)]
        else:
          outputMap[key].append("Password:" + str(idx))

      if(MatchCrypto(line,entropy)):
        if(len(outputMap[key]) == 0):
          outputMap[key] = ["Crypto:" + str(idx)]
        else:
          outputMap[key].append("Crypto:" + str(idx))
      if(MatchBitcion(line,entropy)):
        if(len(outputMap[key]) == 0):
          outputMap[key] = ["Bitcoin:" + str(idx)]
        else:
          outputMap[key].append("Bitcoin:" + str(idx))
      if(MatchEmail(line)):
        if(len(outputMap[key]) == 0):
          outputMap[key] = ["Email:" + str(idx)]
        else:
          outputMap[key].append("Email:" + str(idx))

      idx +=1
            

if __name__ == '__main__':
    pass