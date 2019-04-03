# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 11:24:54 2019

@author: P088904
"""
# 参考
# https://qiita.com/msrks/items/e264872efa062c7d6955

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()

def f(x, y):
    return np.sin(x) + np.cos(y)

x = np.linspace(0, 2 * np.pi, 120)
y = np.linspace(0, 2 * np.pi, 100).reshape(-1, 1)
ims = []

for i in range(60):
    x += np.pi / 15.
    y += np.pi / 20.
    im = plt.imshow(f(x, y), animated=True)
    ims.append([im])

ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True,
                                repeat_delay=1000)

ani.save('anim_dinamic_image.gif', writer="imagemagick")
#ani.save('anim.mp4', writer="ffmpeg")
plt.show()