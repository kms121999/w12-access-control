########################################################################
# COMPONENT:
#    CONTROL
# Author:
#    Br. Helfrich, Kyle Mueller, Keaton Smith, Jake Rammell
# Summary: 
#    This class stores the notion of Bell-LaPadula
########################################################################

Control = {
  "Secret": 3,
  "Privileged": 2,
  "Confidential": 1,
  "Public": 0,
}

def authenticate_read(subject_control, object_control):
  return subject_control >= object_control

def authenticate_write(subject_control, object_control):
  return subject_control <= object_control