from typing import List
import random
import math

class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[float]:
        pts = [tuple(p) for p in trees]
        random.shuffle(pts)

        def dist(a, b):
            return math.hypot(a[0] - b[0], a[1] - b[1])

        def circle2(a, b):
            c = ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2)
            return c, dist(a, b) / 2

        def circle3(a, b, c):
            ax, ay = a
            bx, by = b
            cx, cy = c
            d = 2 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by))
            if abs(d) < 1e-12:
                candidates = [circle2(a, b), circle2(a, c), circle2(b, c)]
                return min(candidates, key=lambda cir: cir[1])
            ux = ((ax * ax + ay * ay) * (by - cy) + (bx * bx + by * by) * (cy - ay) + (cx * cx + cy * cy) * (ay - by)) / d
            uy = ((ax * ax + ay * ay) * (cx - bx) + (bx * bx + by * by) * (ax - cx) + (cx * cx + cy * cy) * (bx - ax)) / d
            center = (ux, uy)
            return center, dist(center, a)

        def inside(cir, p):
            if cir is None:
                return False
            return dist(cir[0], p) <= cir[1] + 1e-9

        circle = None
        for i, p in enumerate(pts):
            if circle is None or not inside(circle, p):
                circle = (p, 0.0)
                for j in range(i):
                    q = pts[j]
                    if not inside(circle, q):
                        circle = circle2(p, q)
                        for k in range(j):
                            r = pts[k]
                            if not inside(circle, r):
                                circle = circle3(p, q, r)
        (x, y), r = circle
        return [x, y, r]
