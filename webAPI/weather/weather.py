#!/usr/bin/env python3
"""simple script to turn a dictionary of weather forecast related values
   into an English description of the forecasr"""

weather =  [{
        'date':'today',
        'state': 'cloudy',
        'temp': 68.5
    },
    {
        'date':'tomorrow',
        'state': 'sunny',
        'temp': 74.8
    }
]

for forecast in weather:
    print(f"The weather for {forecast['date']} will be"
          f" {forecast['state']} with a temperature of {forecast['temp']}")
    
