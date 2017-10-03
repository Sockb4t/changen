'''
Created on 3 Oct 2017

@author: chris
'''

class ChannelStore(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        #                [    0     ,  1   ,     2     ,   3    ,   4    ,  5   ,     6     ,     7     ,    8     ,      9       ,  10  ,  11   ,  12  ,    13   ,   14   ,    15    ,    16    ]
        self.channels = [["Location","Name","Frequency","Duplex","Offset","Tone","rToneFreq","cToneFreq","DtcsCode","DtcsPolarity","Mode","TStep","Skip","Comment","URCALL","RPT1CALL","RPT2CALL"]]
    
    def append(self,channel):
        if (len(channel)+1) == len(self.channels[0]):
            channel.insert(0,str(len(self.channels)))
            self.channels.append(channel)
        else:
            print("ERROR: ChannelStore append method: Provided channel information does not match the required format")
            print(str(len(channel))+" fields provided; "+str(len(self.channels[0])-1)+" fields required.")
    
    def generateSimplex(self, name, count, startFreq, freqStep, mode, comment):
        for i in range(0,count):
            aname = name + "-" + str(i+1)
            afreq = '{:010.6f}'.format(float(startFreq + i * freqStep/1000))
            aduplex = ""
            aoffset = "0.000000"
            atone = ""
            artonefreq = "82.5"
            actonefreq = "82.5"
            adtcscode = "023"
            adtcspol = "NN"
            amode = mode
            atstep = '{:5.2f}'.format(float(freqStep))
            askip = ""
            acomment = comment
            aurcall = ""
            arp1call = ""
            arp2call = "" 
            self.append([aname, afreq, aduplex, aoffset, atone, artonefreq, actonefreq, adtcscode, adtcspol, amode, atstep, askip, acomment, aurcall, arp1call, arp2call])
    
    def addPMR(self):
        self.generateSimplex("PMR-FM", 16, 446.00625, 12.5, "FM", "PMR446 FM")
        self.generateSimplex("PFD-dPMR", 16, 446.103125, 6.25, "FM", "dPMR446 FDMA")
        self.generateSimplex("PTD-DMR", 8, 446.10625, 12.5, "FM", "DMR Tier I TDMA")
    
    def toconsole(self):
        col_width = max(len(word) for channel in self.channels for word in channel) + 2  # padding
        for channel in self.channels:
            print("".join(word.ljust(col_width) for word in channel))
