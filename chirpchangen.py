'''
Created on 3 Oct 2017

@author: chris
'''
from com.sockbat.chirpchangen.channelstore import ChannelStore

if __name__ == '__main__':
    pass

# Memory Naming Convention
#
# A - Air Band
# AV Air Band VHF
# AM Air Band Military
#
# B - Business Radio (Licenced)
# BL Business Radio 
#
# C - Citizen's Band (Licence Free)
# CC CEPT CB Channels
# CD German additional CB Channels
# CU United Kingdom additional CB Channels
# CA Australia's VHF CB Channels
#
# H - Amateur Radio
# HS Ham Simplex
# HR Ham Repeater Channel (Duplex)
# HL Ham Listed Repeater (Duplex)
# HD Ham Digital Modes
#
# M - Maritime
# MV Maritime VHF
# 
# P - Personal / Private Radio
# PMR PMR446 analogue FM Personal Mobile Radio
# PFD dPMR446 FDMA digital Radio
# PTD DMR Tier I TDMA digital Radio

# SAR Frequencies
# 2182 kHz
# 3023 kHz
# 5680 kHz
# 8364 kHz
# 121.5 MHz
# 156.525 MHz, International Distress Safety and Calling DSC
# 156.800 MHz, International Distress Safety and Calling Voice
# 243.000 MHz

# Chirp CSV import format
# Location,Name,Frequency,Duplex,Offset,Tone,rToneFreq,cToneFreq,DtcsCode,DtcsPolarity,Mode,TStep,Skip,Comment,URCALL,RPT1CALL,RPT2CALL
# 1,AV IAD,121.500000,,0.000000,,100.0,100.0,023,NN,AM,25.00,,,,,,
# 2,HS U280 Call,433.500000,,0.000000,,82.5,82.5,023,NN,FM,25.00,,,,,,
# 3,HL GB3XX,433.350000,+,1.600000,Tone,82.5,82.5,023,NN,FM,25.00,,,,,,


chanstore = ChannelStore()

#chanstore.append(["AV IAD","121.500000","","0.000000","","100.0","100.0","023","NN","AM","25.00","","","","",""])
#chanstore.append(["HS U280 Call","433.500000","","0.000000","","82.5","82.5","023","NN","FM","12.50","","","","",""])
#chanstore.append(["HL GB3XX","433.350000","+","1.600000","Tone","82.5","82.5","023","NN","FM","25.00","","","","",""])

#chanstore.addPMR()

chanstore.toconsole()



