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
        self.ft1xd = False
    
    def append(self,channel):
        if len(channel[0]) > 16:    # Channel Name has more than 16 chars
            print("WARNING: Channel " + '{:.16}'.format(channel[0]) + " name shortened as it exceeds 16 characters. Original name: " + channel[0])
            channel[0] = '{:.16}'.format(channel[0])
        if (len(channel)+1) == len(self.channels[0]):
            channel.insert(0,str(len(self.channels)))
            self.channels.append(channel)
        else:
            print("ERROR: ChannelStore append method: Provided channel information does not match the required format")
            print(str(len(channel))+" fields provided; "+str(len(self.channels[0])-1)+" fields required.")
    
    def generateSimplex(self, name, count, startFreq, freqStep, mode, comment, start=1):
        for i in range(0,count):
            aname = name + "-" + str(i+start)
            afreq = '{:9.6f}'.format(float(startFreq + i * freqStep/1000))
            aduplex = ""
            aoffset = "0.000000"
            atone = ""
            artonefreq = "82.5"
            actonefreq = "82.5"
            adtcscode = "023"
            adtcspol = "NN"
            amode = mode
            atstep = '{:4.2f}'.format(float(freqStep))
            askip = ""
            acomment = comment
            aurcall = ""
            arp1call = ""
            arp2call = "" 
            self.append([aname, afreq, aduplex, aoffset, atone, artonefreq, actonefreq, adtcscode, adtcspol, amode, atstep, askip, acomment, aurcall, arp1call, arp2call])

    def addAir(self):
        freqStep = 0.025
        mode = "FM"
        comment = "AIR VHF"
        aduplex = ""
        aoffset = "0.000000"
        atone = ""
        artonefreq = "82.5"
        actonefreq = "82.5"
        adtcscode = "023"
        adtcspol = "NN"
        amode = mode
        atstep = '{:4.2f}'.format(float(freqStep*1000))
        askip = ""
        acomment = comment
        aurcall = ""
        arp1call = ""
        arp2call = ""

        aname = "AVHF-CH001"
        afreq = '{:010.6f}'.format(float("118.0"))
        self.append([aname, afreq, aduplex, aoffset, atone, artonefreq, actonefreq, adtcscode, adtcspol, amode, atstep, askip, acomment, aurcall, arp1call, arp2call])
        
        aname = "AVHF-IAD-SAR"
        afreq = '{:010.6f}'.format(float("121.5"))
        self.append([aname, afreq, aduplex, aoffset, atone, artonefreq, actonefreq, adtcscode, adtcspol, amode, atstep, askip, acomment, aurcall, arp1call, arp2call])

        aname = "AVHF-FRS"
        afreq = '{:010.6f}'.format(float("121.6"))
        self.append([aname, afreq, aduplex, aoffset, atone, artonefreq, actonefreq, adtcscode, adtcspol, amode, atstep, askip, acomment, aurcall, arp1call, arp2call])

        aname = "AVHF-AFIS"
        afreq = '{:010.6f}'.format(float("122.4"))
        self.append([aname, afreq, aduplex, aoffset, atone, artonefreq, actonefreq, adtcscode, adtcspol, amode, atstep, askip, acomment, aurcall, arp1call, arp2call])

        aname = "AVHF-Air2Air-Fixed"
        afreq = '{:010.6f}'.format(float("122.75"))
        self.append([aname, afreq, aduplex, aoffset, atone, artonefreq, actonefreq, adtcscode, adtcspol, amode, atstep, askip, acomment, aurcall, arp1call, arp2call])

        aname = "AVHF-SAR-Training"
        afreq = '{:010.6f}'.format(float("122.9"))
        self.append([aname, afreq, aduplex, aoffset, atone, artonefreq, actonefreq, adtcscode, adtcspol, amode, atstep, askip, acomment, aurcall, arp1call, arp2call])

        aname = "AVHF-Special"
        afreq = '{:010.6f}'.format(float("122.925"))
        self.append([aname, afreq, aduplex, aoffset, atone, artonefreq, actonefreq, adtcscode, adtcspol, amode, atstep, askip, acomment, aurcall, arp1call, arp2call])
        
        aname = "AVHF-Air2Air-Heli"
        afreq = '{:010.6f}'.format(float("123.025"))
        self.append([aname, afreq, aduplex, aoffset, atone, artonefreq, actonefreq, adtcscode, adtcspol, amode, atstep, askip, acomment, aurcall, arp1call, arp2call])

        aname = "AVHF-SAR"
        afreq = '{:010.6f}'.format(float("123.1"))
        self.append([aname, afreq, aduplex, aoffset, atone, artonefreq, actonefreq, adtcscode, adtcspol, amode, atstep, askip, acomment, aurcall, arp1call, arp2call])
        
        aname = "AVHF-Flight-School"
        afreq = '{:010.6f}'.format(float("123.3"))
        self.append([aname, afreq, aduplex, aoffset, atone, artonefreq, actonefreq, adtcscode, adtcspol, amode, atstep, askip, acomment, aurcall, arp1call, arp2call])

        aname = "AVHF-12345"
        afreq = '{:010.6f}'.format(float("123.45"))
        self.append([aname, afreq, aduplex, aoffset, atone, artonefreq, actonefreq, adtcscode, adtcspol, amode, atstep, askip, acomment, aurcall, arp1call, arp2call])
        
        aname = "AVHF-Flight-School"
        afreq = '{:010.6f}'.format(float("123.5"))
        self.append([aname, afreq, aduplex, aoffset, atone, artonefreq, actonefreq, adtcscode, adtcspol, amode, atstep, askip, acomment, aurcall, arp1call, arp2call])

        aname = "AM-Military-Advisory"
        afreq = '{:010.6f}'.format(float("126.2"))
        self.append([aname, afreq, aduplex, aoffset, atone, artonefreq, actonefreq, adtcscode, adtcspol, amode, atstep, askip, acomment, aurcall, arp1call, arp2call])

        aname = "AVHF-Multicom-Australia"
        afreq = '{:010.6f}'.format(float("126.7"))
        self.append([aname, afreq, aduplex, aoffset, atone, artonefreq, actonefreq, adtcscode, adtcspol, amode, atstep, askip, acomment, aurcall, arp1call, arp2call])

        aname = "AM-Military-Advisory"
        afreq = '{:010.6f}'.format(float("134.1"))
        self.append([aname, afreq, aduplex, aoffset, atone, artonefreq, actonefreq, adtcscode, adtcspol, amode, atstep, askip, acomment, aurcall, arp1call, arp2call])

        aname = "AVFH-VOLMET"
        afreq = '{:010.6f}'.format(float("135.375"))
        self.append([aname, afreq, aduplex, aoffset, atone, artonefreq, actonefreq, adtcscode, adtcspol, amode, atstep, askip, acomment, aurcall, arp1call, arp2call])

        aname = "AM-MAD-SAR"
        afreq = '{:010.6f}'.format(float("243.0"))
        self.append([aname, afreq, aduplex, aoffset, atone, artonefreq, actonefreq, adtcscode, adtcspol, amode, atstep, askip, acomment, aurcall, arp1call, arp2call])

        aname = "AM-MEP"
        afreq = '{:010.6f}'.format(float("245.1"))
        self.append([aname, afreq, aduplex, aoffset, atone, artonefreq, actonefreq, adtcscode, adtcspol, amode, atstep, askip, acomment, aurcall, arp1call, arp2call])

    def addMarine(self):
        # Channel 0
        aname = "MVHF-0-HMCG"
        freqStep = 0.050
        mode = "FM"
        comment = "Maritime VHF"
        afreq = '{:010.6f}'.format(float("156.0"))
        aduplex = "+"
        aoffset = "4.600000"
        atone = ""
        artonefreq = "82.5"
        actonefreq = "82.5"
        adtcscode = "023"
        adtcspol = "NN"
        amode = mode
        atstep = '{:4.2f}'.format(float(freqStep*1000))
        askip = ""
        acomment = comment
        aurcall = ""
        arp1call = ""
        arp2call = ""
        self.append([aname, afreq, aduplex, aoffset, atone, artonefreq, actonefreq, adtcscode, adtcspol, amode, atstep, askip, acomment, aurcall, arp1call, arp2call])
          
        # Channels 1 - 28
        for i in range(0,28):
            name = "MVHF"
            startFreq = "156.050"
            mode = "FM"
            if i == 15:
                aname = name + "-" + str(i+1) + "-Distress" 
            else:
                aname = name + "-" + str(i+1)
            afreq = '{:010.6f}'.format(float(startFreq) + i * freqStep)
            if i == 5 or i >=7 and i<=16:
                aduplex = ""
                aoffset = "0.000000"
            else:
                aduplex = "+"
                aoffset = "4.600000"
            self.append([aname, afreq, aduplex, aoffset, atone, artonefreq, actonefreq, adtcscode, adtcspol, amode, atstep, askip, acomment, aurcall, arp1call, arp2call])
        
        # Channel 31
        aname = "MVHF-31"
        afreq = '{:010.6f}'.format(float("157.550"))
        aduplex = "+"
        aoffset = "4.600000"
        self.append([aname, afreq, aduplex, aoffset, atone, artonefreq, actonefreq, adtcscode, adtcspol, amode, atstep, askip, acomment, aurcall, arp1call, arp2call])
        
        # Channel 37A/M1
        aname = "MVHF-37A-M1"
        afreq = '{:010.6f}'.format(float("157.850"))
        aduplex = ""
        aoffset = "0.000000"
        self.append([aname, afreq, aduplex, aoffset, atone, artonefreq, actonefreq, adtcscode, adtcspol, amode, atstep, askip, acomment, aurcall, arp1call, arp2call])
        
        # Channels 60 - 88
        for i in range(0,29):
            startFreq = "156.025"
            mode = "FM"
            afreq = '{:010.6f}'.format(float(startFreq) + i * freqStep)
            if i == 10:
                aname = name + "-" + str(i+60) + "-Distress-DSC"
            else:
                aname = name + "-" + str(i+60)
            if i==27 or i ==28 or i >=7 and i<=17:
                aduplex = ""
                aoffset = "0.000000"
            else:
                aduplex = "+"
                aoffset = "4.600000"
            self.append([aname, afreq, aduplex, aoffset, atone, artonefreq, actonefreq, adtcscode, adtcspol, amode, atstep, askip, acomment, aurcall, arp1call, arp2call])

        # Channel M2/P4
        aname = "MVHF-M2-P4"
        afreq = '{:010.6f}'.format(float("161.425"))
        aduplex = ""
        aoffset = "0.000000"
        self.append([aname, afreq, aduplex, aoffset, atone, artonefreq, actonefreq, adtcscode, adtcspol, amode, atstep, askip, acomment, aurcall, arp1call, arp2call])

        # Channel 87B
        aname = "MVHF-87B-AIS"
        afreq = '{:010.6f}'.format(float("161.975"))
        self.append([aname, afreq, aduplex, aoffset, atone, artonefreq, actonefreq, adtcscode, adtcspol, amode, atstep, askip, acomment, aurcall, arp1call, arp2call])
                        
        # Channel 88B
        aname = "MVHF-88B-AIS"
        afreq = '{:010.6f}'.format(float("162.025"))
        self.append([aname, afreq, aduplex, aoffset, atone, artonefreq, actonefreq, adtcscode, adtcspol, amode, atstep, askip, acomment, aurcall, arp1call, arp2call])
       
        # Channel 99
        aname = "MVHF-99-HMCG"
        afreq = '{:010.6f}'.format(float("160.600"))
        self.append([aname, afreq, aduplex, aoffset, atone, artonefreq, actonefreq, adtcscode, adtcspol, amode, atstep, askip, acomment, aurcall, arp1call, arp2call])
        
        # Channel M (Lifeguards)
        aname = "MVHF-Lifeguards"
        afreq = '{:010.6f}'.format(float("161.225"))
        self.append([aname, afreq, aduplex, aoffset, atone, artonefreq, actonefreq, adtcscode, adtcspol, amode, atstep, askip, acomment, aurcall, arp1call, arp2call])
        
        # UK172 - 132.65 MHz +/- 12.5kHz is used by HMCG for communication with SAR helicopters.
        freqStep = 0.0125
        atstep = '{:4.2f}'.format(float(freqStep*1000))
        aname = "MVHF-HMCG"
        afreq = '{:010.6f}'.format(float("132.6375"))
        self.append([aname, afreq, aduplex, aoffset, atone, artonefreq, actonefreq, adtcscode, adtcspol, amode, atstep, askip, acomment, aurcall, arp1call, arp2call])
        afreq = '{:010.6f}'.format(float("132.6500"))
        self.append([aname, afreq, aduplex, aoffset, atone, artonefreq, actonefreq, adtcscode, adtcspol, amode, atstep, askip, acomment, aurcall, arp1call, arp2call])
        afreq = '{:010.6f}'.format(float("132.6625"))
        self.append([aname, afreq, aduplex, aoffset, atone, artonefreq, actonefreq, adtcscode, adtcspol, amode, atstep, askip, acomment, aurcall, arp1call, arp2call])

        # Channel 99
        aname = "MUHF-EPIRB"
        afreq = '{:010.6f}'.format(float("406.025"))
        self.append([aname, afreq, aduplex, aoffset, atone, artonefreq, actonefreq, adtcscode, adtcspol, amode, atstep, askip, acomment, aurcall, arp1call, arp2call])
 
        if not self.ft1xd:
            # MW Distress Frequencies
            aname = "MMW-Distress"
            amode = "AM"
            freqStep = 0.001
            atstep = '{:4.2f}'.format(float(freqStep*1000))
            afreq = '{:010.6f}'.format(float("2.1820"))
            self.append([aname, afreq, aduplex, aoffset, atone, artonefreq, actonefreq, adtcscode, adtcspol, amode, atstep, askip, acomment, aurcall, arp1call, arp2call])
            afreq = '{:010.6f}'.format(float("3.023"))
            self.append([aname, afreq, aduplex, aoffset, atone, artonefreq, actonefreq, adtcscode, adtcspol, amode, atstep, askip, acomment, aurcall, arp1call, arp2call])
            afreq = '{:010.6f}'.format(float("5.680"))
            self.append([aname, afreq, aduplex, aoffset, atone, artonefreq, actonefreq, adtcscode, adtcspol, amode, atstep, askip, acomment, aurcall, arp1call, arp2call])
            afreq = '{:010.6f}'.format(float("8.364"))
            self.append([aname, afreq, aduplex, aoffset, atone, artonefreq, actonefreq, adtcscode, adtcspol, amode, atstep, askip, acomment, aurcall, arp1call, arp2call])
     
    def addCustom(self):
        self.append(["POCSAG-PageOne","153.350000","","0.000000","","82.5","82.5","023","NN","FM","12.50","S","POCSAG","","",""])
        self.append(["Binatone550-Ch9","447.006250","","0.000000","","82.5","82.5","023","NN","FM","6.25","","hidden channel","","",""])
        
        freqStep = 0.0125
        mode = "FM"
        comment = "FRS"
        aduplex = ""
        aoffset = "0.000000"
        atone = ""
        artonefreq = "82.5"
        actonefreq = "82.5"
        adtcscode = "023"
        adtcspol = "NN"
        amode = mode
        atstep = '{:4.2f}'.format(float(freqStep*1000))
        askip = ""
        acomment = comment
        aurcall = ""
        arp1call = ""
        arp2call = ""

        aname = "FRS-"
        for freq in [(457.0125,457.0125,"C3"),(457.0375,457.0375,"C1"),(457.0875,462.5875,"C2"),(457.1375,462.6375,"C5"),(457.1875,457.1875,"C4"),(457.2375,457.2375,"C6")]:  
            afreq = '{:010.6f}'.format(float(freq[0]))    
            offsetval = float(freq[1]) - float(freq[0]) #txfreq - rxfreq = offset value
            aoffset = '{:8.6f}'.format(abs(offsetval))
            if freq[0] == freq[1]:
                aduplex = ""
            elif offsetval > 0.0001:
                aduplex = "+"
            elif offsetval < -0.0001:
                aduplex = "-"
            else:
                aduplex = ""
            self.append([aname+freq[2], afreq, aduplex, aoffset, atone, artonefreq, actonefreq, adtcscode, adtcspol, amode, atstep, askip, acomment, aurcall, arp1call, arp2call])



        for freq in [450.230000,460.330000,462.130000,462.230000,462.330000,462.430000,462.530000,462.630000,462.730000,462.830000,462.930000, 
                     463.030000,463.130000,463.230000,463.530000,469.950000]:
            afreq = '{:010.6f}'.format(float(freq))
            aname = "BF-888-"+afreq
            acomment = "BF-888 factory CHs"
            atstep = "10.00"
            self.append([aname, afreq, aduplex, aoffset, atone, artonefreq, actonefreq, adtcscode, adtcspol, amode, atstep, askip, acomment, aurcall, arp1call, arp2call])


        for freq in [("BOS218-THW",167.900000), ("BOS220-KatS",167.940000), ("BOS225-KatS",168.040000), 
                     ("BOS231-ZusA",168.160000), ("BOS232-KatS",168.180000), ("BOS234-KatS",168.220000), 
                     ("BOS246-KatS",168.460000), ("BOS249-HiOrg",168.520000), ("BOS250-FW",168.540000), 
                     ("BOS251-HiOrg",168.560000), ("BOS253-FW",168.600000), ("BOS255-FW",168.640000), 
                     ("BOS256-FW",168.660000)]:
            afreq = '{:010.6f}'.format(float(freq[1]))
            aname = freq[0]
            aduplex = "+"
            aoffset = "4.600000"
            atstep = "20.00"
            acomment = "BOS 2m"
            self.append([aname, afreq, aduplex, aoffset, atone, artonefreq, actonefreq, adtcscode, adtcspol, amode, atstep, askip, acomment, aurcall, arp1call, arp2call])
  
  
    def addBusinessRadio(self):
        freqStep = 0.0125
        mode = "FM"
        comment = "Business Radio Suppliers Light"
        aduplex = ""
        aoffset = "0.000000"
        atone = ""
        artonefreq = "82.5"
        actonefreq = "82.5"
        adtcscode = "023"
        adtcspol = "NN"
        amode = mode
        atstep = '{:4.2f}'.format(float(freqStep*1000))
        askip = ""
        acomment = comment
        aurcall = ""
        arp1call = ""
        arp2call = ""

        for freq in [(82.125,68.625),(85.875,72.375),(163.2875,158.7875),(163.6875,159.1875),(163.7500,159.2500),(163.8500,159.3500), 
                     (163.9000,159.4000),(163.9250,159.4250),(163.9500,159.4500),(167.2000,172.0000),(453.6875,460.1875), 
                     (454.4250,461.4250),(456.3875,461.8875),(456.9875,462.4875),(456.0125,461.5125),(456.3375,461.8375), 
                     (456.4625,461.9625),(456.5625,462.0625),(456.6875,462.1875),(456.9250,462.4250),(456.9625,462.4625)]:
            afreq = '{:010.6f}'.format(float(freq[0]))
            aname = "BRSL-"+afreq
            offsetval = float(freq[1]) - float(freq[0]) #txfreq - rxfreq = offset value
            aoffset = '{:8.6f}'.format(abs(offsetval))
            if freq[0] == freq[1]:
                aduplex = ""
            elif offsetval > 0.0001:
                aduplex = "+"
            elif offsetval < -0.0001:
                aduplex = "-"
            else:
                aduplex = ""     
            self.append([aname, afreq, aduplex, aoffset, atone, artonefreq, actonefreq, adtcscode, adtcspol, amode, atstep, askip, acomment, aurcall, arp1call, arp2call])
 
        for freq in [26.8350,26.9200,48.9750,48.9875,68.6250,72.3750,82.1250,85.8750,158.7875,159.1875,159.2500,159.3500,159.4500,
                     159.4875,159.5000,159.5875,159.6250,159.6875,163.2875,163.6875,163.7500,163.8500,163.9000,163.9250,163.9500, 
                     163.9875,164.0000,164.0875,164.1250,164.1875,167.2000,169.0125,169.1375,169.1625,169.1875,172.000,453.6875, 
                     454.4250,456.3875,456.8625,456.9250,456.9875,460.1875,461.4250,461.8875,462.3625,462.4250,462.4750]:
            afreq = '{:010.6f}'.format(float(freq))
            aname = "BRSL-"+afreq
            aduplex = ""
            aoffset = "0.000000"     
            self.append([aname, afreq, aduplex, aoffset, atone, artonefreq, actonefreq, adtcscode, adtcspol, amode, atstep, askip, acomment, aurcall, arp1call, arp2call])
 
        acomment = "Business Radio Simple Site"  
        for freq in range(0,4126,125):
            afreq = "49."+'{:04d}'.format(freq)+"00"
            aname = "BRSS-"+afreq
            aduplex = ""
            aoffset = "0.000000"     
            self.append([aname, afreq, aduplex, aoffset, atone, artonefreq, actonefreq, adtcscode, adtcspol, amode, atstep, askip, acomment, aurcall, arp1call, arp2call])         
        afreq = "49.487500"
        aname = "BRSS-"+afreq
        self.append([aname, afreq, aduplex, aoffset, atone, artonefreq, actonefreq, adtcscode, adtcspol, amode, atstep, askip, acomment, aurcall, arp1call, arp2call])
        
        if not self.ft1xd:
            for freq in [26.2375, 26.41,26.4375,26.4625,26.545,26.588, 
                         26.6155,26.6695,26.7255,26.8155,26.8655,26.865]:
                afreq = '{:9.6f}'.format(float(freq))
                aname = "BRSS-"+afreq
                aduplex = ""
                aoffset = "0.000000"     
                self.append([aname, afreq, aduplex, aoffset, atone, artonefreq, actonefreq, adtcscode, adtcspol, amode, atstep, askip, acomment, aurcall, arp1call, arp2call])         

        for freq in [159.6375, 159.65, 159.6625, 159.675, 159.7, 161.0,
                     161.0125, 161.025, 161.0375, 161.05, 161.0625, 161.075,
                     161.0875, 161.1, 161.1125, 164.2]:
            afreq = '{:010.6f}'.format(float(freq))
            aname = "BRSS-"+afreq
            aduplex = ""
            aoffset = "0.000000"     
            self.append([aname, afreq, aduplex, aoffset, atone, artonefreq, actonefreq, adtcscode, adtcspol, amode, atstep, askip, acomment, aurcall, arp1call, arp2call])         
   
        for freq in [459.05, 459.1, 459.125, 459.15, 459.175, 459.2,
                     459.225, 459.25, 459.275, 459.3, 459.325, 459.35,
                     459.375, 459.4, 459.425, 459.45, 459.475]:
            afreq = '{:010.6f}'.format(float(freq))
            aname = "BRSS-"+afreq
            aduplex = ""
            aoffset = "0.000000"     
            self.append([aname, afreq, aduplex, aoffset, atone, artonefreq, actonefreq, adtcscode, adtcspol, amode, atstep, askip, acomment, aurcall, arp1call, arp2call])       
            
        acomment = "Business Radio Simple UK"
        for freq in [77.687500,86.337500,86.350000,86.362500,86.375000,164.050000,164.062500,169.087500,169.312500,173.050000, 
                     173.062500,173.087500,449.312500,449.400000,449.475000]:
            afreq = '{:010.6f}'.format(float(freq))
            aname = "BRSU-"+afreq
            aduplex = ""
            aoffset = "0.000000"     
            self.append([aname, afreq, aduplex, aoffset, atone, artonefreq, actonefreq, adtcscode, adtcspol, amode, atstep, askip, acomment, aurcall, arp1call, arp2call])         
        
    def addPMR(self):
        self.generateSimplex("PMR", 16, 446.00625, 12.5, "FM", "PMR446 FM")
        if not self.ft1xd:
            self.generateSimplex("PMD", 16, 446.103125, 6.25, "FM", "dPMR446 FDMA") # deactivated as not programmable for Yaesu UHF radios
        self.generateSimplex("PDMR", 8, 446.10625, 12.5, "Auto", "DMR Tier I TDMA")
    
    def addFreenet(self):
        self.generateSimplex("PFR", 3, 149.025, 12.5, "FM", "Freenet FM (DE)")
        self.generateSimplex("PFR", 3, 149.0875, 12.5, "FM", "Freenet FM (DE)",start=4)
        if not self.ft1xd:
            self.generateSimplex("PFD", 6, 149.021875, 6.25, "Auto", "Freenet FM (DE)")
            self.generateSimplex("PFD", 6, 149.084375, 6.25, "Auto", "Freenet FM (DE)",start=7)

    def addRaynet(self):
        aname = "HSE-Raynet-80m"
        freqStep = 0.001
        atstep = '{:4.2f}'.format(float(freqStep*1000))
        amode = "AM"
        acomment = "Raynet"
        afreq = '{:8.6f}'.format(float("3.663"))
        aduplex = ""
        aoffset = "0.000000"
        atone = ""
        artonefreq = "82.5"
        actonefreq = "82.5"
        adtcscode = "023"
        adtcspol = "NN"
        askip = ""
        aurcall = ""
        arp1call = ""
        arp2call = ""
        if not self.ft1xd:
            self.append([aname, afreq, aduplex, aoffset, atone, artonefreq, actonefreq, adtcscode, adtcspol, amode, atstep, askip, acomment, aurcall, arp1call, arp2call])
        
        aname = "HSE-Raynet-40m"
        amode = "AM"
        afreq = '{:8.6f}'.format(float("7.110"))
        self.append([aname, afreq, aduplex, aoffset, atone, artonefreq, actonefreq, adtcscode, adtcspol, amode, atstep, askip, acomment, aurcall, arp1call, arp2call])

        aname = "HSE-Raynet-6m"
        amode = "FM"
        for freq in [51.65,51.75,51.77,51.79]:
            afreq = '{:8.6f}'.format(float(freq))
            self.append([aname, afreq, aduplex, aoffset, atone, artonefreq, actonefreq, adtcscode, adtcspol, amode, atstep, askip, acomment, aurcall, arp1call, arp2call])

        aname = "HSE-Raynet-4m"
        amode = "FM"
        for freq in [70.350,70.375,70.400]:
            afreq = '{:8.6f}'.format(float(freq))
            self.append([aname, afreq, aduplex, aoffset, atone, artonefreq, actonefreq, adtcscode, adtcspol, amode, atstep, askip, acomment, aurcall, arp1call, arp2call])

        aname = "HSE-Raynet-2m"
        if not self.ft1xd:
            amode = "USB"
            afreq = '{:8.6f}'.format(float("144.260"))
            self.append([aname, afreq, aduplex, aoffset, atone, artonefreq, actonefreq, adtcscode, adtcspol, amode, atstep, askip, acomment, aurcall, arp1call, arp2call])
        amode = "FM" 
        for freq in [144.625, 144.650, 144.675, 144.775, 144.800, 145.200, 145.255]:
            afreq = '{:8.6f}'.format(float(freq))
            self.append([aname, afreq, aduplex, aoffset, atone, artonefreq, actonefreq, adtcscode, adtcspol, amode, atstep, askip, acomment, aurcall, arp1call, arp2call])

        aname = "HSE-Raynet-70cm"
        amode = "FM"
        for freq in [433.700, 433.725, 433.750, 433.775]:
            afreq = '{:8.6f}'.format(float(freq))
            self.append([aname, afreq, aduplex, aoffset, atone, artonefreq, actonefreq, adtcscode, adtcspol, amode, atstep, askip, acomment, aurcall, arp1call, arp2call])
        
        aname = "HRE-Raynet-70cm"
        for freq in [(438.4,430.8),(432.775,434.375)]:  # 2x pairs of Raynet Repeater frequencies
            afreq = '{:8.6f}'.format(float(freq[0]))    
            offsetval = float(freq[1]) - float(freq[0]) #txfreq - rxfreq = offset value
            aoffset = '{:8.6f}'.format(abs(offsetval))
            if freq[0] == freq[1]:
                aduplex = ""
            elif offsetval > 0.0001:
                aduplex = "+"
            elif offsetval < -0.0001:
                aduplex = "-"
            else:
                aduplex = ""
            self.append([aname, afreq, aduplex, aoffset, atone, artonefreq, actonefreq, adtcscode, adtcspol, amode, atstep, askip, acomment, aurcall, arp1call, arp2call])

    def addHam6m(self):
        amode = "FM"
        acomment = "Amateur Radio"
        atone = ""
        artonefreq = "82.5"
        actonefreq = "82.5"
        adtcscode = "023"
        adtcspol = "NN"
        askip = ""
        aurcall = ""
        arp1call = ""
        arp2call = ""
        name = "HS6-"
        freqStep = 0.01
        atstep = '{:4.2f}'.format(float(freqStep*1000))
        for freq in [(50.510,"SSTV-AFSK"),
                     (50.520,"Inetgate"),
                     (50.530,"Inetgate"),
                     (50.540,"Inetgate"),
                     (50.550,"Image-Fax"),
                     (50.600,"RTTY-FSK")]:
            aname = name+freq[1]
            afreq = '{:9.6f}'.format(float(freq[0]))
            aduplex = ""
            aoffset = "0.000000"
            self.append([aname, afreq, aduplex, aoffset, atone, artonefreq, actonefreq, adtcscode, adtcspol, amode, atstep, askip, acomment, aurcall, arp1call, arp2call])
        
        for freq in range(50620,50751,10):
            aname = name+"DV-"+str(float(freq)/1000)
            afreq = '{:9.6f}'.format(float(freq)/1000)
            if afreq == "50.630000":
                aname = "HS6-DVCALL-50.63"
            aduplex = ""
            aoffset = "0.000000"
            self.append([aname, afreq, aduplex, aoffset, atone, artonefreq, actonefreq, adtcscode, adtcspol, amode, atstep, askip, acomment, aurcall, arp1call, arp2call])
    
        for freq in range(50710,50891,10):
            aname = "HR6-"+str(float(freq)/1000)
            afreq = '{:9.6f}'.format(float(freq)/1000)
            aduplex = "+"
            aoffset = "0.500000"
            self.append([aname, afreq, aduplex, aoffset, atone, artonefreq, actonefreq, adtcscode, adtcspol, amode, atstep, askip, acomment, aurcall, arp1call, arp2call])

        for freq in range(51410,51591,20):
            aname = "HS6-FMDV-"+str(float(freq)/1000)
            afreq = '{:9.6f}'.format(float(freq)/1000)
            if afreq == "51.510000":
                aname = "HS6-FMCALL-51.51"
            aduplex = ""
            aoffset = "0.000000"
            self.append([aname, afreq, aduplex, aoffset, atone, artonefreq, actonefreq, adtcscode, adtcspol, amode, atstep, askip, acomment, aurcall, arp1call, arp2call])

        for freq in range(51810,51991,10):
            aname = "HR6-IARU-"+str(float(freq)/1000)
            afreq = '{:9.6f}'.format(float(freq)/1000)
            aduplex = ""
            aoffset = "0.000000"
            self.append([aname, afreq, aduplex, aoffset, atone, artonefreq, actonefreq, adtcscode, adtcspol, amode, atstep, askip, acomment, aurcall, arp1call, arp2call])

    def addHam4m(self):
        amode = "FM"
        acomment = "Amateur Radio"
        atone = ""
        artonefreq = "82.5"
        actonefreq = "82.5"
        adtcscode = "023"
        adtcspol = "NN"
        askip = ""
        aurcall = ""
        arp1call = ""
        arp2call = ""
        name = "HS4-"
        freqStep = 0.0125
        atstep = '{:4.2f}'.format(float(freqStep*1000))
        for freq in [(70.2600,"AM-FM-CALL"),
                     (70.3000,"All-Modes"),
                     (70.3125,"Digital"),
                     (70.3250,"DX-Cluster"),
                     (70.3375,"Digital"),
                     (70.3625,"Inetgate"),
                     (70.3875,"Inetgate"),
                     (70.4125,"Inetgate"),
                     (70.4250,"FM-Simplex"),
                     (70.4375,"Digital"),
                     (70.4500,"FM-CALL"),
                     (70.4625,"Digital"),
                     (70.4750,"All-Modes"),
                     (70.4875,"Digital")]:
            aname = name+freq[1]
            afreq = '{:9.6f}'.format(float(freq[0]))
            aduplex = ""
            aoffset = "0.000000"
            self.append([aname, afreq, aduplex, aoffset, atone, artonefreq, actonefreq, adtcscode, adtcspol, amode, atstep, askip, acomment, aurcall, arp1call, arp2call])
        
    def addHam2m(self):
        amode = "FM"
        acomment = "Amateur Radio"
        atone = ""
        artonefreq = "82.5"
        actonefreq = "82.5"
        adtcscode = "023"
        adtcspol = "NN"
        askip = ""
        aurcall = ""
        arp1call = ""
        arp2call = ""
        name = "HS2-"
        freqStep = 0.0125
        atstep = '{:4.2f}'.format(float(freqStep*1000))
        for freq in [(144.5000,"SSTV"),
                     (144.6000,"RTTY"),
                     (144.6125,"DV-CALL"),
                     (144.7500,"ATV-TB"),
                     (144.8000,"APRS"),
                     (144.8125,"DV-Inetgate"),
                     (144.8250,"DV-Inetgate"),
                     (144.8375,"DV-Inetgate"),
                     (144.8500,"DV-Inetgate"),
                     (144.8625,"DV-Inetgate"),
                     (144.9250,"TCP-IP"),
                     (144.9375,"AX25"),
                     (144.9500,"AX25"),
                     (144.9625,"FM-Inetgate"),
                     (145.2000,"V16-Space-Comms"),
                     ]:
            aname = name+freq[1]
            afreq = '{:9.6f}'.format(float(freq[0]))
            aduplex = ""
            aoffset = "0.000000"
            self.append([aname, afreq, aduplex, aoffset, atone, artonefreq, actonefreq, adtcscode, adtcspol, amode, atstep, askip, acomment, aurcall, arp1call, arp2call])

        for freq in range(1452125,1455876,125):
            aname = "HS2-V"+str(((freq-1452125)/125)+17)+"-"+str(float(freq)/10000)
            if freq == 1455000:
                aname="HS2-V40-FM-CALL"
            afreq = '{:9.6f}'.format(float(freq)/10000)
            aduplex = ""
            aoffset = "0.000000"
            self.append([aname, afreq, aduplex, aoffset, atone, artonefreq, actonefreq, adtcscode, adtcspol, amode, atstep, askip, acomment, aurcall, arp1call, arp2call])
 
        for freq in [(145.8000,"Space-Comms"),
                     ]:
            aname = name+freq[1]
            afreq = '{:9.6f}'.format(float(freq[0]))
            aduplex = ""
            aoffset = "0.000000"
            self.append([aname, afreq, aduplex, aoffset, atone, artonefreq, actonefreq, adtcscode, adtcspol, amode, atstep, askip, acomment, aurcall, arp1call, arp2call])

 
        for freq in range(1456000,1457876,125):
            aname = "HR2-R"+str(((freq-1456000)/125)+48)+"-"+str(float(freq)/10000)
            afreq = '{:9.6f}'.format(float(freq)/10000)
            aduplex = "-"
            aoffset = "0.600000"
            self.append([aname, afreq, aduplex, aoffset, atone, artonefreq, actonefreq, adtcscode, adtcspol, amode, atstep, askip, acomment, aurcall, arp1call, arp2call])
 
    def addHam70cm(self):
        amode = "FM"
        acomment = "Amateur Radio"
        atone = ""
        artonefreq = "82.5"
        actonefreq = "82.5"
        adtcscode = "023"
        adtcspol = "NN"
        askip = ""
        aurcall = ""
        arp1call = ""
        arp2call = ""
        name = "HS7-"
        freqStep = 0.0125
        atstep = '{:4.2f}'.format(float(freqStep*1000))
        for freq in [(430.0125,"FM-Inetgate"),
                     (430.0250,"FM-Inetgate"),
                     (430.0375,"FM-Inetgate"),
                     (430.0500,"FM-Inetgate"),
                     (430.0625,"FM-Inetgate"),
                     (430.0750,"FM-Inetgate")]:
            aname = name+freq[1]
            afreq = '{:9.6f}'.format(float(freq[0]))
            aduplex = ""
            aoffset = "0.000000"
            self.append([aname, afreq, aduplex, aoffset, atone, artonefreq, actonefreq, adtcscode, adtcspol, amode, atstep, askip, acomment, aurcall, arp1call, arp2call])

        for freq in range(4308250,4309751,125):
            aname = "HR7-RU"+str(((freq-4308250)/125)+66)+"-"+str(float(freq)/10000)
            afreq = '{:9.6f}'.format(float(freq)/10000)
            aduplex = "+"
            aoffset = "7.600000"
            self.append([aname, afreq, aduplex, aoffset, atone, artonefreq, actonefreq, adtcscode, adtcspol, amode, atstep, askip, acomment, aurcall, arp1call, arp2call])
 
        for freq in range(4309750,4319000,125):
            aname = "HD7-DV-"+str(float(freq)/10000)
            afreq = '{:9.6f}'.format(float(freq)/10000)
            aduplex = ""
            aoffset = "0.000000"
            self.append([aname, afreq, aduplex, aoffset, atone, artonefreq, actonefreq, adtcscode, adtcspol, amode, atstep, askip, acomment, aurcall, arp1call, arp2call])

        for freq in range(4326250,4326751,250):
            aname = "HD7-DV-"+str(float(freq)/10000)
            afreq = '{:9.6f}'.format(float(freq)/10000)
            aduplex = ""
            aoffset = "0.000000"
            self.append([aname, afreq, aduplex, aoffset, atone, artonefreq, actonefreq, adtcscode, adtcspol, amode, atstep, askip, acomment, aurcall, arp1call, arp2call])

        for freq in range(4330000,4333751,250):
            aname = "HR7-RB"+str(((freq-4330000)/250)+0)+"-"+str(float(freq)/10000)
            afreq = '{:9.6f}'.format(float(freq)/10000)
            aduplex = "+"
            aoffset = "1.600000"
            self.append([aname, afreq, aduplex, aoffset, atone, artonefreq, actonefreq, adtcscode, adtcspol, amode, atstep, askip, acomment, aurcall, arp1call, arp2call])

        for freq in [(433.4000,"U272"),
                     (433.4250,"U274"),
                     (433.4500,"U276"),
                     (433.4750,"U278"),
                     (433.5000,"U280-FM-CALL"),
                     (433.5250,"U282"),
                     (433.5500,"U284"),
                     (433.5750,"U286"),
                     (433.6000,"U288-AFSK")
                     ]:
            aname = "HS7-"+freq[1]
            afreq = '{:9.6f}'.format(float(freq[0]))
            aduplex = ""
            aoffset = "0.000000"
            self.append([aname, afreq, aduplex, aoffset, atone, artonefreq, actonefreq, adtcscode, adtcspol, amode, atstep, askip, acomment, aurcall, arp1call, arp2call])

        for freq in range(4336250,4336751,250):
            aname = "HD7-"+str(float(freq)/10000)
            afreq = '{:9.6f}'.format(float(freq)/10000)
            aduplex = ""
            aoffset = "0.000000"
            self.append([aname, afreq, aduplex, aoffset, atone, artonefreq, actonefreq, adtcscode, adtcspol, amode, atstep, askip, acomment, aurcall, arp1call, arp2call])

        for freq in range(4338000,4342501,125):
            aname = "HD7-"+str(float(freq)/10000)
            afreq = '{:9.6f}'.format(float(freq)/10000)
            aduplex = ""
            aoffset = "0.000000"
            self.append([aname, afreq, aduplex, aoffset, atone, artonefreq, actonefreq, adtcscode, adtcspol, amode, atstep, askip, acomment, aurcall, arp1call, arp2call])

        for freq in range(4344750,4345251,125):
            aname = "HS7-Inet-"+str(float(freq)/10000)
            afreq = '{:9.6f}'.format(float(freq)/10000)
            aduplex = ""
            aoffset = "0.000000"
            self.append([aname, afreq, aduplex, aoffset, atone, artonefreq, actonefreq, adtcscode, adtcspol, amode, atstep, askip, acomment, aurcall, arp1call, arp2call])

        for freq in range(4380250,4381751,250):
            aname = "HD7-"+str(float(freq)/10000)
            afreq = '{:9.6f}'.format(float(freq)/10000)
            aduplex = ""
            aoffset = "0.000000"
            self.append([aname, afreq, aduplex, aoffset, atone, artonefreq, actonefreq, adtcscode, adtcspol, amode, atstep, askip, acomment, aurcall, arp1call, arp2call])

        for freq in [(438.6125,"DV-CALL")
                     ]:
            aname = "HD7-"+freq[1]
            afreq = '{:9.6f}'.format(float(freq[0]))
            aduplex = ""
            aoffset = "0.000000"
            self.append([aname, afreq, aduplex, aoffset, atone, artonefreq, actonefreq, adtcscode, adtcspol, amode, atstep, askip, acomment, aurcall, arp1call, arp2call])

        for freq in range(4394000,4397751,250):
            aname = "HR7-DR"+str(((freq-4330000)/250)+0)+"-"+str(float(freq)/10000)
            afreq = '{:9.6f}'.format(float(freq)/10000)
            aduplex = "-"
            aoffset = "9.000000"
            self.append([aname, afreq, aduplex, aoffset, atone, artonefreq, actonefreq, adtcscode, adtcspol, amode, atstep, askip, acomment, aurcall, arp1call, arp2call])

        for freq in range(4398000,4400001,250):
            aname = "HD7-"+str(float(freq)/10000)
            afreq = '{:9.6f}'.format(float(freq)/10000)
            aduplex = ""
            aoffset = "0.000000"
            self.append([aname, afreq, aduplex, aoffset, atone, artonefreq, actonefreq, adtcscode, adtcspol, amode, atstep, askip, acomment, aurcall, arp1call, arp2call])


    
    def toconsole(self):
        col_width = max(len(word) for channel in self.channels for word in channel) + 2  # padding
        for channel in self.channels:
            print("".join(word.ljust(col_width) for word in channel))
