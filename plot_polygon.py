# -*- coding:utf-8 -*-
"""
@author : LT
@date   : 2021-06-21
@desc   : plot polygon
"""
import matplotlib.pyplot as plt
import numpy as np


def read_polygon(file):
    points = []
    with open(file, 'r') as f:
        for line in f.readlines():
            line = line.strip()
            if line is not '':
                line_arr = line.split(',')
                points.append((float(line_arr[0]), float(line_arr[1])))
    return points

def plot_polygon(points, save_png_file):
    x = np.array(points)[:,0]
    y = np.array(points)[:,1]
    
    plt.plot(x, y, marker='.')
    ax = plt.gca()
    ax.set_aspect(1)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data',0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data',0))

    plt.legend()
    plt.title('polygon')
    plt.savefig(save_png_file)


if __name__ == "__main__":
    points = read_polygon('polygon.txt')
    plot_polygon(points, 'polygon.png')