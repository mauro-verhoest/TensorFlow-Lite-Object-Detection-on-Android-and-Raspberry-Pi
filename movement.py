import numpy as np
import math


class Movement:
    """Allows the stepper motor to move"""

    def __init__(self, lamda, focal_length, rho, resolution):
        # Lamda (lambda) is a multiplying factor for the speed at which the camera should rotate
        self.lamda = lamda
        # Focal length is the focal length of the camera used
        self.focal_length = focal_length
        # Rho is the pixel size
        self.rho = rho
        # Resolution is the resolution of the camera
        if resolution == tuple or list:
            self.resolution = resolution

    def move_horizontal(self, xcoord, ycoord):
        u = xcoord
        v = ycoord
        coord = (u, v)
        center = (int(self.resolution[0]/2), int(self.resolution[1]/2))
        pe = (coord[0] - center[0], coord[1] - center[1])
        l = self.lamda
        f = self.focal_length
        r = self.rho
        jp = np.array([[(r*u*v)/f, -(f*f+r*r*u*u)/(r*f)],
                       [(f*f+r*r*v*v)/(r*f), -(r*u*v)/f]])
        inv_jp = np.linalg.pinv(jp)
        speed = l*inv_jp*pe
        rpm = speed*2*math.pi/60
        rotate = 'XXXXX'
        print(rpm)
        return 't:00000r:' + rotate + 's:' + str(round(rpm[1][0]))

    def move_vertical(self, xcoord, ycoord):
        u = xcoord
        v = ycoord
        coord = (u, v)
        center = (int(self.resolution[0] / 2), int(self.resolution[1] / 2))
        pe = (coord[0] - center[0], coord[1] - center[1])
        l = self.lamda
        f = self.focal_length
        r = self.rho
        jp = np.array([[(r * u * v) / f, -(f * f + r * r * u * u) / (r * f)],
                       [(f * f + r * r * v * v) / (r * f), -(r * u * v) / f]])
        inv_jp = np.linalg.pinv(jp)
        speed = l * inv_jp * pe
        rpm = speed * 2 * math.pi / 60
        print(rpm)
        return 't:' + tilt + 'r:00000s:' + str(rpm[0])
