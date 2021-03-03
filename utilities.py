from scipy.spatial import distance
from constants import *

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

def calc_delay(distance, atmo = None):
    ''' Converts meters to seconds according to speed of sound ''' 
    return  distance / SPEED_OF_SOUND

def correct_speed_of_sound(humidity, )
