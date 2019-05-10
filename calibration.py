#import loadcell_config as loadcell
import filter

no_readings = 100

while(1):
    try:
        known_sg1 = float(input('Please enter a known specific gravity for the 1st. point of calibration: '))
        break
    except ValueError:
        print('You have not entered a number')

print('Measuring. Wait until prompted')
known_data1 = filter.filterData(loadcell.getreadings(no_readings))
print('Measuring done')

while(1):
    try:
        known_sg2 = float(input('Please enter a known specific gravity for the 2nd. point of calibration: '))
        if known_sg1 == known_sg2:
            continue
        break
    except ValueError:
        print('You have not entered a number')

print('Measuring. Wait until prompted')
known_data2 = filter.filterData(loadcell.getreadings(no_readings))
print('Measuring done')

if known_sg1 > known_sg2:
    scale_factor = (known_sg1 - known_sg2)/(known_data1 - known_data2)
else:
    scale_factor = (known_sg2 - known_sg1)/(known_data2 - known_data1)

print('Scale factor: {:f}'.format(scale_factor))
