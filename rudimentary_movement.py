# Author: Rembie01
# Date: 8 dec 2020


class Movement:
    """Allows the stepper motor to move"""

    def __init__(self, factor=1, fov_angle_horizontal=62, fov_angle_vertical=37, resolution=(1280, 720), play=1):
        self.factor = factor
        self.h_angle = fov_angle_horizontal
        self.v_angle = fov_angle_vertical
        self.res = resolution
        self.play = play
        self.direction = '-'

    def move_horizontal(self, xcoord):
        self.direction = '-'
        rotate_pixels = -(xcoord - self.res[0]/2)
        pixels_per_degree = self.res[0] / self.h_angle
        rotate = round(rotate_pixels / pixels_per_degree)
        if rotate < 0:
            self.direction = '+'
            rotate = -rotate
        if rotate <= self.play:
            return 't:00r:00s:0000td:0rd:0'
        if len(str(rotate)) <= 1:
            rotate = '0' + str(rotate)
        rpm = self.factor * rotate
        while len(str(rpm)) <= 3:
            rpm = '0' + str(rpm)
        return 't:00r:' + str(rotate) + 's:' + str(rpm) + 'td:0rd:' + self.direction

    def move_vertical(self, ycoord):
        self.direction = '-'
        tilt_pixels = -(ycoord - self.res[1] / 2)
        pixels_per_degree = self.res[1] / self.v_angle
        tilt = round(tilt_pixels / pixels_per_degree)
        if tilt < 0:
            self.direction = '+'
            tilt = -tilt
        if tilt <= self.play:
            return 't:00r:00s:0000td:0rd:0'
        if len(str(tilt)) <= 1:
            tilt = '0' + str(tilt)
        rpm = self.factor * tilt
        while len(str(rpm)) <= 3:
            rpm = '0' + str(rpm)
        return 't:' + str(tilt) + 'r:00s:' + str(rpm) + 'td:' + self.direction + 'rd:0'
