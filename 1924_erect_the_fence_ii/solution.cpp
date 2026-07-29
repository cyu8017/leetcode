// LeetCode 1924 - Erect the Fence II
#include <algorithm>
#include <cmath>
#include <random>
#include <utility>
#include <vector>

class Solution {
    using Pt = std::pair<double, double>;
    double dist(Pt a, Pt b) {
        return std::hypot(a.first - b.first, a.second - b.second);
    }
    std::pair<Pt, double> circle2(Pt a, Pt b) {
        Pt c{(a.first + b.first) / 2, (a.second + b.second) / 2};
        return {c, dist(a, b) / 2};
    }
    std::pair<Pt, double> circle3(Pt a, Pt b, Pt c) {
        double ax = a.first, ay = a.second, bx = b.first, by = b.second, cx = c.first, cy = c.second;
        double d = 2 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by));
        if (std::abs(d) < 1e-12) {
            auto c1 = circle2(a, b), c2 = circle2(a, c), c3 = circle2(b, c);
            auto best = c1;
            if (c2.second < best.second) best = c2;
            if (c3.second < best.second) best = c3;
            return best;
        }
        double ux = ((ax * ax + ay * ay) * (by - cy) + (bx * bx + by * by) * (cy - ay) + (cx * cx + cy * cy) * (ay - by)) / d;
        double uy = ((ax * ax + ay * ay) * (cx - bx) + (bx * bx + by * by) * (ax - cx) + (cx * cx + cy * cy) * (bx - ax)) / d;
        Pt center{ux, uy};
        return {center, dist(center, a)};
    }
    bool inside(const std::pair<Pt, double>& cir, Pt p) {
        return dist(cir.first, p) <= cir.second + 1e-9;
    }
public:
    std::vector<double> outerTrees(std::vector<std::vector<int>>& trees) {
        std::vector<Pt> pts;
        for (auto& t : trees) pts.emplace_back(t[0], t[1]);
        std::mt19937 rng(42);
        std::shuffle(pts.begin(), pts.end(), rng);
        std::pair<Pt, double> circle{{0, 0}, -1};
        for (int i = 0; i < (int)pts.size(); i++) {
            if (circle.second < 0 || !inside(circle, pts[i])) {
                circle = {pts[i], 0.0};
                for (int j = 0; j < i; j++) {
                    if (!inside(circle, pts[j])) {
                        circle = circle2(pts[i], pts[j]);
                        for (int k = 0; k < j; k++) {
                            if (!inside(circle, pts[k])) circle = circle3(pts[i], pts[j], pts[k]);
                        }
                    }
                }
            }
        }
        return {circle.first.first, circle.first.second, circle.second};
    }
};
