import numpy as np
import matplotlib.pyplot as plt

class Torus:
    def __init__(self, R, r, theta1, theta2):
        self.R = R
        self.r = r
        self.theta1 = theta1
        self.theta2 = theta2
        self.length = self.torus_geodesic_length()
        self.plot_torus()
        print("Geodesic length between theta1 and theta2:", self.length)
        
    def torus_geodesic_length(self):
        phi1 = self.theta1 * 2 * np.pi
        phi2 = self.theta2 * 2 * np.pi
        cos_phi_diff = np.cos(phi1 - phi2)
        length = np.sqrt((self.R + self.r * cos_phi_diff)**2 + (self.r * np.sin(phi1 - phi2))**2)
        return length

    def plot_torus(self):
        u = np.linspace(0, 2 * np.pi, 100)
        v = np.linspace(0, 2 * np.pi, 100)
        u, v = np.meshgrid(u, v)
        x = (self.R + self.r * np.cos(v)) * np.cos(u)
        y = (self.R + self.r * np.cos(v)) * np.sin(u)
        z = self.r * np.sin(v)
        
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(x, y, z, cmap='viridis')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        
        plt.show()

if __name__ == "__main__":
    # トーラスの主半径
    R = 5

    # トーラスの管の半径
    r = 2

    # 2点間を結ぶ角度パラメータ
    theta1 = 0.25
    theta2 = 0.75

    # トーラスのオブジェクトを作成し、初期化
    torus = Torus(R, r, theta1, theta2)
