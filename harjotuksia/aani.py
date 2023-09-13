#tehdään hiukan äänijuttuja

import winsound

#demotaan ajan yli tapahtuvaa prosessia

print("nyt tapahtuu jotakin ....")
winsound.Beep(440, 1000)
print("... ja nyt se tapahtui!")

for i in range(10):
    print("nyt jotakin pientä asiaa...")
    winsound.Beep(1000+i*100,100)
    print("... ja siinä se lyhyt juttu soi")