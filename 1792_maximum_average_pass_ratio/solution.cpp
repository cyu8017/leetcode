// LeetCode 1792 - Maximum Average Pass Ratio
// https://leetcode.com/problems/maximum-average-pass-ratio/

#include <queue>
#include <tuple>
#include <vector>

class Solution {
public:
    double maxAverageRatio(std::vector<std::vector<int>>& classes, int extraStudents) {
        auto gain = [](double p, double t) {
            return (p + 1) / (t + 1) - p / t;
        };
        std::priority_queue<std::tuple<double, double, double>> heap;
        for (const auto& cls : classes) {
            double p = cls[0];
            double t = cls[1];
            heap.emplace(gain(p, t), p, t);
        }
        for (int i = 0; i < extraStudents; i++) {
            auto [g, p, t] = heap.top();
            heap.pop();
            p += 1;
            t += 1;
            heap.emplace(gain(p, t), p, t);
        }
        double total = 0;
        while (!heap.empty()) {
            auto [g, p, t] = heap.top();
            heap.pop();
            total += p / t;
        }
        return total / classes.size();
    }
};
