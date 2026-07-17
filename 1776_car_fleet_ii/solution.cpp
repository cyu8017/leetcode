// LeetCode 1776 - Car Fleet II
// https://leetcode.com/problems/car-fleet-ii/

#include <vector>

class Solution {
public:
    std::vector<double> getCollisionTimes(std::vector<std::vector<int>>& cars) {
        int n = (int)cars.size();
        std::vector<double> ans(n, -1.0);
        std::vector<int> stack;
        for (int i = n - 1; i >= 0; i--) {
            int pos = cars[i][0];
            int speed = cars[i][1];
            while (!stack.empty()) {
                int j = stack.back();
                if (speed <= cars[j][1]) {
                    stack.pop_back();
                    continue;
                }
                double t = (double)(cars[j][0] - pos) / (speed - cars[j][1]);
                if (ans[j] < 0 || t <= ans[j]) {
                    ans[i] = t;
                    break;
                }
                stack.pop_back();
            }
            stack.push_back(i);
        }
        return ans;
    }
};
