def two_fer(name=None):
        
    sentence = "One for you, one for me." 

    if name != None:
        sentence =  "One for {}, one for me.".format(name)

    return sentence



