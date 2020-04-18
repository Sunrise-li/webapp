from snow_flake import SnowFlake
import time;

snow_flake = SnowFlake()
start = round(time.time()*1000)

i = 0;
while True:
    snow_flake.id()
    i += 1
    if round(time.time()*1000)-start == 1000:
        break

end = round(time.time()*1000)

print('count : {0}'.format(i))
print(end - start)