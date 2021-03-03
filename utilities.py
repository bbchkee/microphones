from scipy.spatial import distance

class Geometry(object):
    ''' Contains information about coordinates of microphones 
        and functions for calculating the distance from mic to signal source'''
        
    def __init__(self, coordinates = []):
        ''' coordinates = [ [x1,y1,z1], [x2,y2,z2], ...] '''
        self.coordinates = coordinates        
    
    def calc_distances(geometry, signal_positions):
        ''' Calculates distance from mic to signal source by given coordinates'''
        distances = []
        for signal_position in signal_positions:
            for mic in geometry.coordinates:
                distances.append(distance.euclidean(signal_position, mic))
        return distances

