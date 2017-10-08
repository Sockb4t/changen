'''
Created on 3 Oct 2017

@author: chris
'''
import csv
from mhlib import isnumeric

class CSVfileIO(object):
    '''
    classdocs
    '''


    def __init__(self, filename):
        '''
        Constructor
        '''
        self.name = filename
        
    def openw(self):
        self.outp = open(self.name, 'w')
        
    def openr(self):
        self.inp = open(self.name, 'r')
        self.csvr = csv.reader(self.inp)
        
    def close(self):
        self.outp.close()
        
    def linew(self, line):
        csv.writer(self.outp, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONE).writerow(line)
        
    def writestore(self, store):    
        self.openw()
        for channel in store.channels:
            self.linew(channel)
        self.close()
    
#    def is_number(self,s):
#        try:
#            float(s)
#            return True
#        except ValueError:
#            return False
       
    def readukrpt(self, store, region=""):
        self.openr()
        
        for record in self.csvr:
            if record[0] == "repeater" and record[1] == "band" and record[2] == "channel" and record[3] == "TX" and record[4] == "RX":  # First line of csv
                continue
            if float(record[3]) < 0.5 or float(record[3]) > 999.999:    # Skip frequencies out of range
                continue
            if record[5] == "DSTAR" or record[5] == "DV":            # Skip incompatible modes
                continue
            lregion = record[9]
            if not (lregion == region or region == ""):               # Skip if a region was specified and this record does not match
                continue            
            callsign = record[0]
            # band = record[1]
            # chan = record[2]
            rxfreq = '{:10.6f}'.format(float(record[3]))
            txfreq = record[4]
            offsetval = float(record[4]) - float(record[3]) #txfreq - rxfreq = offset value
            offsetnum = '{:8.6f}'.format(abs(offsetval))
            if rxfreq == txfreq:
                offsetdir = ""
            elif offsetval > 0.0001:
                offsetdir = "+"
            elif offsetval < -0.0001:
                offsetdir = "-"
            else:
                offsetdir = ""
            if record[5] == "AV" or record[5] == "MULTI":
                mode = "FM"
            else:
                mode = "Auto"
            freqstep = "12.50"
            # locator = record[6]
            location = record[7]
            # ngr = record[8]

            ccode = record[10]            
            if mode == "FM" and ccode != "" and isnumeric(ccode[0]) and float(ccode) > 66 and float(ccode) < 255:    # CTCSS Tone Freq
                fcode = '{:5.1f}'.format(float(ccode))
                tone = "Tone"
            else:
                fcode = "82.5"
                tone = ""
            # keeper = record[11]
            # lat = record[12]
            # lon = record[13]
            store.append([""+callsign+" "+location,rxfreq,offsetdir,offsetnum,tone,fcode,fcode,"754","NN",mode,freqstep,"","","","",""])