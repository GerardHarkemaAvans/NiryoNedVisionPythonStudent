#!/usr/bin/env python
import math


def get_angle_2_points(x1, y1, x2, y2):
    """
    angle of the line starting at (x1,y1) and finishing at (x2,y2), according to repere trigonometrique
    :param x1: x position of the first point
    :param y1: y position of the first point
    :param x2: x position of the second point
    :param y2: y position of the second point
    :return: angle in radians
    """
    dy = float(y2) - float(y1)
    dx = float(x2) - float(x1)
    if dx == 0:
        # return 90 if dy > 0 else -90
        return math.pi / 2 if dy > 0 else -math.pi / 2

    else:
        return math.atan2(dy, dx)


def euclidean_dist(x1, y1, x2, y2):
    """
    Return euclidean distance between 2 points
    :param x1: x position of the first point
    :param y1: y position of the first point
    :param x2: x position of the second point
    :param y2: y position of the second point
    :return: distance in the same metrics as the points
    """
    return math.sqrt((float(x1) - float(x2)) ** 2 + (float(y1) - float(y2)) ** 2)


def euclidean_dist_2_pts(p1, p2):
    """
    Return euclidean distance between 2 points
    :param p1: tuple(X,Y) of the first point's coordinates
    :param p2: tuple(X,Y) of the second point's coordinates
    :return: distance in the same metrics as the points
    """
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((float(x1) - float(x2)) ** 2 + (float(y1) - float(y2)) ** 2)


def euclidean_3d_dist(p1, p2):
    """
    Return euclidean 3d distance between 2 points
    :param p1: Point of the first point's coordinates
    :param p2: Point of the second point's coordinates
    :return: distance in the same metrics as the points
    """
    return math.sqrt(
        (float(p1.x) - float(p2.x)) ** 2 + (float(p1.y) - float(p2.y)) ** 2 + (float(p1.z) - float(p2.z)) ** 2)

'''
def calculate_barycenter(list_points):
    """
    Return barycenter of a list of points

    :param list_points: list of Point
    """
    from geometry_msgs.msg import Point
    barycenter = Point()
    for point in list_points:
        barycenter.x += point.x
        barycenter.y += point.y
        barycenter.z += point.z

    barycenter.x = barycenter.x / len(list_points)
    barycenter.y = barycenter.y / len(list_points)
    barycenter.z = barycenter.z / len(list_points)

    return barycenter
'''
