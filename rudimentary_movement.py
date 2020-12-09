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

    def move_horizontal(self, xcoord):
        rotate_pixels = -(xcoord - self.res[0] / 2)
        pixels_per_degree = self.res[0] / self.h_angle
        rotate = round(rotate_pixels / pixels_per_degree)
        if rotate <= self.play:
            return '00,00,0000'
        if len(str(rotate)) <= 1:
            rotate = '0' + str(rotate)
        rpm = self.factor * rotate
        while len(str(rpm)) <= 3:
            rpm = '0' + str(rpm)
        return '00,' + str(rotate) + ',' + str(rpm)

    def move_vertical(self, ycoord):
        tilt_pixels = -(ycoord - self.res[1] / 2)
        pixels_per_degree = self.res[1] / self.v_angle
        tilt = round(tilt_pixels / pixels_per_degree)
        if tilt <= self.play:
            return '00,00,0000'
        if len(str(tilt)) <= 1:
            tilt = '0' + str(tilt)
        rpm = self.factor * tilt
        while len(str(rpm)) <= 3:
            rpm = '0' + str(rpm)
        return str(tilt) + ',00,' + str(rpm)

    def move(self, xcoord, ycoord):
        rotate_pixels = -(xcoord - self.res[0] / 2)
        tilt_pixels = -(ycoord - self.res[1] / 2)
        rotate_pixels_per_degree = self.res[0] / self.h_angle
        tilt_pixels_per_degree = self.res[1] / self.v_angle
        rotate = round(rotate_pixels / rotate_pixels_per_degree)
        tilt = round(tilt_pixels / tilt_pixels_per_degree)
        if rotate <= self.play and tilt <= self.play:
            return '00,00,0000,0000'
        if rotate <= self.play:
            if len(str(tilt)) <= 1:
                tilt = '0' + str(tilt)
            tilt_rpm = self.factor * tilt
            while len(str(tilt_rpm)) <= 3:
                tilt_rpm = '0' + str(tilt_rpm)
            return str(tilt) + ',00,' + str(tilt_rpm) + ',0000'
        if tilt <= self.play:
            if len(str(rotate)) <= 1:
                rotate = '0' + str(rotate)
            rotate_rpm = self.factor * rotate
            while len(str(rotate_rpm)) <= 3:
                rotate_rpm = '0' + str(rotate_rpm_rpm)
            return '00,' + str(rotate) + ',0000,' + str(rotate_rpm)
        if len(str(rotate)) <= 1:
            rotate = '0' + str(rotate)
        if len(str(tilt)) <= 1:
            tilt = '0' + str(tilt)
        rotate_rpm = self.factor * rotate
        tilt_rpm = self.factor * tilt
        while len(str(rotate_rpm)) <= 3:
            rotate_rpm = '0' + str(rotate_rpm)
        while len(str(tilt_rpm)) <= 3:
            tilt_rpm = '0' + str(tilt_rpm)
        return str(tilt) + ',' + str(rotate) + ',' + str(tilt_rpm) + ',' + str(rotate_rpm)
