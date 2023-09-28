
def get_hour(epoch_seconds):
    hour = epoch_seconds // 3600
    return hour
# double slash performs floor division, rounding result to nearest integer
def get_minutes(epoch_seconds):
   minutes = epoch_seconds // 60 % 60
   return minutes

def get_seconds(epoch_seconds):
   seconds = epoch_seconds % 3600 % 60
   return seconds
# test case ex: 3800s / 3600s will have R200s...R200s / 60s will have R20s

    
    
    