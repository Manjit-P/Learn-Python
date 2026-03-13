# Understanding tuple as record.

lax_coordinates = (33.9435, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32_450, 0.66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]
for passport in sorted(traveler_ids):
    
    # print(passport) ('BRA', 'CE342567')
    print(passport) # 'BRA', 'CE342567'