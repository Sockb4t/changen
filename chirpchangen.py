'''
Created on 3 Oct 2017

@author: chris
'''
from com.sockbat.chirpchangen.channelstore import ChannelStore
from com.sockbat.chirpchangen import fileio

if __name__ == '__main__':
    pass

chanstore = ChannelStore()
chanstore.ft1xd = True

chanstore.addAir()
chanstore.addMarine()
chanstore.addCustom()
chanstore.addBusinessRadio()
chanstore.addPMR()
chanstore.addFreenet()
chanstore.addRaynet()
chanstore.addHam6m()
chanstore.addHam4m()
chanstore.addHam2m()
chanstore.addHam70cm()

fileio.CSVfileIO("ukrepeaters.csv").readukrpt(chanstore,"SE")
fileio.CSVfileIO("ukrepeaters.csv").readukrpt(chanstore,"SW")
fileio.CSVfileIO("ukrepeaters.csv").readukrpt(chanstore,"MIDL")

fileio.CSVfileIO("channels.csv").writestore(chanstore)

chanstore.toconsole()



