# Understanding match pattern.

metro_areas = [
 ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
 ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
 ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
 ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
]
for record in metro_areas:
    match record:
        case [name, _, _, (lat, lon)] if lon <= 0: # Pattern matching
            print(f'{name:15}| {lat:9.4f}| {lon:9.4f}')

# Sequence pattern can be enclosed with either brackets (), [].