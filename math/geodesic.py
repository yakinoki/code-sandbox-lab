# coding: utf-8
"""球面上の 2 点間の最短距離を求め、可視化するモジュール。"""

import math
from typing import Sequence, Tuple
import matplotlib.pyplot as plt
import numpy as np


Vector3 = Tuple[float, float, float]


def input_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("数値を入力してください。")


def point_on_sphere_from_xy(x: float, y: float, radius: float) -> Vector3:
    squared = radius ** 2 - x ** 2 - y ** 2
    if squared < 0:
        raise ValueError("x と y の値が半径を超えています。")
    return x, y, math.sqrt(squared)


def spherical_coordinates(point: Vector3) -> Tuple[float, float]:
    x, y, z = point
    longitude = math.atan2(y, x)
    latitude = math.atan2(z, math.hypot(x, y))
    return latitude, longitude


def great_circle_distance(point1: Vector3, point2: Vector3, radius: float) -> float:
    dot = sum(a * b for a, b in zip(point1, point2))
    cos_angle = max(-1.0, min(1.0, dot / (radius ** 2)))
    return radius * math.acos(cos_angle)


def generate_geodesic_curve(point1: Vector3, point2: Vector3, radius: float, steps: int = 100) -> np.ndarray:
    p1 = np.array(point1) / radius
    p2 = np.array(point2) / radius
    cos_angle = float(np.dot(p1, p2))
    cos_angle = max(-1.0, min(1.0, cos_angle))
    omega = math.acos(cos_angle)
    if omega < 1e-12:
        return np.tile(np.array(point1), (steps, 1))

    sin_omega = math.sin(omega)
    t = np.linspace(0.0, 1.0, steps)
    curve = [
        (math.sin((1.0 - tt) * omega) / sin_omega) * p1
        + (math.sin(tt * omega) / sin_omega) * p2
        for tt in t
    ]
    return np.vstack(curve) * radius


def plot_geodesic(points: Sequence[Vector3], radius: float) -> None:
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = radius * np.outer(np.cos(u), np.sin(v))
    y = radius * np.outer(np.sin(u), np.sin(v))
    z = radius * np.outer(np.ones_like(u), np.cos(v))
    ax.plot_surface(x, y, z, color="cyan", alpha=0.15, edgecolor="none")

    geodesic = generate_geodesic_curve(points[0], points[1], radius)
    ax.plot(geodesic[:, 0], geodesic[:, 1], geodesic[:, 2], color="red", linewidth=2, label="Geodesic")

    xs, ys, zs = zip(*points)
    ax.scatter(xs, ys, zs, c="blue", s=80, label="Points")
    for idx, (x_val, y_val, z_val) in enumerate(points, start=1):
        ax.text(x_val, y_val, z_val, f"P{idx}")

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_title("Sphere Geodesic")
    ax.legend()
    ax.set_box_aspect([1, 1, 1])
    plt.show()


def main() -> None:
    radius = input_float("半径 r を入力してください: ")
    print(f"半径は {radius} です。\n")

    points: list[Vector3] = []
    for index in range(1, 3):
        x = input_float(f"{index}点目の x 座標を入力してください: ")
        y = input_float(f"{index}点目の y 座標を入力してください: ")
        point = point_on_sphere_from_xy(x, y, radius)
        latitude, longitude = spherical_coordinates(point)

        print(f"{index}点目の座標: {point}")
        print(f"緯度: {latitude:.6f}, 経度: {longitude:.6f}\n")
        points.append(point)

    distance = great_circle_distance(points[0], points[1], radius)
    print(f"二点間の球面上の最短距離: {distance:.6f}\n")

    plot_geodesic(points, radius)


if __name__ == "__main__":
    main()

