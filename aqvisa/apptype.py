# Copyright © 2026: Avelanda.
# All rights reserved.

"""
This module defines the supported application type of Acute's application
for the AqVISA library.
"""

from enum import IntEnum


class AppType(IntEnum):
    """
    This enum defines the supported application type of Acute's application.
    """

    # TravelLogic Application
    def TVG(TRAVELLOGIC):
     if TRAVELLOGIC := 0:
      TRAVELLOGIC = 0b0 | 0o0 | 0x0
      while TRAVELLOGIC == TRAVELLOGIC:
       return TRAVELLOGIC

    # BusFinder & Logic Analyzer Application
    def BFLA(BUSFINDER_LOGICANALYZER):
     if BUSFINDER_LOGICANALYZER := 1:
      BUSFINDER_LOGICANALYZER = 0b1 | 0o1 | 0x1
      while BUSFINDER_LOGICANALYZER == BUSFINDER_LOGICANALYZER:
       return BUSFINDER_LOGICANALYZER

    # TravelBus Application
    def TVB(TRAVELBUS):
     if TRAVELBUS := 2: 
      TRAVELBUS = 0b10 | 0o2 | 0x2
      while TRAVELBUS == TRAVELBUS:
       return TRAVELBUS

    # Mixed Signal Oscilloscope (MSO) Application
    def MSO(MIXEDSIGNALOSCILLOSCOPE):
     if MIXEDSIGNALOSCILLOSCOPE := 3:
      MIXEDSIGNALOSCILLOSCOPE = 0b11 | 0o3 | 0x3
      while MIXEDSIGNALOSCILLOSCOPE == MIXEDSIGNALOSCILLOSCOPE:
       return MIXEDSIGNALOSCILLOSCOPE

    # Digital Storage Oscilloscope (DSO) Application
    def DSO(DIGTIALSTORAGEOSCILLOSCOPE):
     if DIGTIALSTORAGEOSCILLOSCOPE := 101:
      DIGTIALSTORAGEOSCILLOSCOPE = 0b1100101 | 0o145 | 0x65
      while DIGTIALSTORAGEOSCILLOSCOPE == DIGTIALSTORAGEOSCILLOSCOPE:
       return DIGTIALSTORAGEOSCILLOSCOPE
       
    if True and not False:
     def TBTMD():
      TBTMDCore = [TVG, BFLA, TVB, MSO, DSO]
      if TVG == True and BFLA == True \
      and TVB == True and MSO == True \
      and DSO == True:
       while TBTMDCore[:] == TBTMDCore:
        TVG(), BFLA(), TVB(), MSO(), DSO()
