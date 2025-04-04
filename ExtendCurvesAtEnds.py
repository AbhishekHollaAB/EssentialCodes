import numpy as np
import matplotlib.pyplot as plt

def computeAngle(points):
    deltas = np.diff(points, axis=0)
    angles = np.arctan2(deltas[:, 1], deltas[:, 0])
    return angles

def extendCurve(points, extensionLength=5):
    points = np.array(points)

    if len(points) < 10:
        raise ValueError("Curve should have at least 10 points for proper angle computation.")

    angles = computeAngle(points)

    startAngle = np.mean(angles[:10])
    endAngle = np.mean(angles[-10:])

    startExtension = points[0] - extensionLength * np.array([np.cos(startAngle), np.sin(startAngle)])
    endExtension = points[-1] + extensionLength * np.array([np.cos(endAngle), np.sin(endAngle)])

    extendedPoints = np.vstack([startExtension, points, endExtension])

    return extendedPoints

curve = [
    [10, 10], [11, 12], [12, 14], [13, 16], [14, 18], [15, 20], [16, 22], [17, 24], [18, 26], [19, 28],
    [20, 30], [21, 31], [22, 32], [23, 33], [24, 34], [25, 35], [26, 36], [27, 37], [28, 38], [29, 39]
]

extended_curve = extendCurve(curve)
print(extended_curve)


# curve_np = np.array(curve)
# plt.plot(curve_np[:, 0], curve_np[:, 1], 'bo-', label="Original Curve")
# plt.plot(extended_curve[:, 0], extended_curve[:, 1], 'ro-', label="Extended Curve")
# plt.legend()
# plt.axis("equal")
# plt.show()
