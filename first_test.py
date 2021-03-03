import utilities

signal_coordinates = [ [0,  0,-50],
                       [50, 0,-50],
                       [100,0,-50],
                       [150,0,-50],
                       [200,0,-50],
                       [250,0,-50] ]

mic_coordinates = [ [0,0,0] , [250,0,0] ] 

stereopair = utilities.Geometry(mic_coordinates)
distances = stereopair.calc_distances(signal_coordinates)
print(distances)
