import numpy as np


class Movement:
    """Allows the stepper motor to move"""

    def __init__(self, lamda, focal_length, rho):
        # Lamda (lambda) is a multiplying factor for the speed at which the camera should rotate
        self.lamda = lamda
        # Focal length is the focal length of the camera used
        self.focal_length = focal_length
        # Rho is the pixel size
        self.rho = rho

    def move_left(self, xcoord, ycoord):
        jp = np.a
        return 't:00000r:' + rotate + 's:' + rpm

    def move_right(self, xcoord, ycoord):

        return 't:00000r:' + rotate + 's:' + rpm

    def move_up(self, xcoord, ycoord):

        return 't:' + tilt + 'r:00000s:' + rpm

    def move_down(self, xcoord, ycoord):

        return 't:' + tilt + 'r:00000s:' + rpm
