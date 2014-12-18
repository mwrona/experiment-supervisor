import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import numpy
from numpy.core.numeric import zeros

def create_chart(x_surface, y_surface, z_surface, x_res, y_res, z_res, fun_name):
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    ax.plot_surface(x_surface, y_surface, z_surface, cstride=1, rstride=1, cmap=cm.coolwarm, \
                    linewidth=0, antialiased=False)

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    ax.plot(x_res, y_res, z_res, 'ro')

    #plt.savefig(fun_name + ".jpg")
    plt.show()

def equidistant_nodes(a, b, n):
    return map(lambda x: a + (b - a) * float(x) / (n - 1), range(0, n))


def draw(fun, a, b, name, x_res, y_res, z_res):
    t_x = equidistant_nodes(a[0], b[0], 101)
    t_y = equidistant_nodes(a[1], b[1], 101)

    x_surface, y_surface = numpy.meshgrid(t_x, t_y)
    z_surface = zeros((len(x_surface), len(x_surface[0])))
    for i in xrange(0, len(x_surface)):
        for j in xrange(0, len(x_surface[0])):
            z_surface[i][j] = fun([x_surface[i][j], y_surface[i][j]])

    create_chart(x_surface, y_surface, z_surface, [x_res], [y_res], [z_res], name)