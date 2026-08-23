// LeetCode 3647 - Maximum Weight in Two Bags
// https://leetcode.com/problems/maximum-weight-in-two-bags/

#include <algorithm>
#include <vector>

class Solution {
public:
    int maxWeight(std::vector<int>& weights, int w1, int w2) {
        std::vector<std::vector<int>> f(w1 + 1, std::vector<int>(w2 + 1));
        for (int x : weights) {
            for (int j = w1; j >= 0; j--) {
                for (int k = w2; k >= 0; k--) {
                    if (x <= j) f[j][k] = std::max(f[j][k], f[j - x][k] + x);
                    if (x <= k) f[j][k] = std::max(f[j][k], f[j][k - x] + x);
                }
            }
        }
        return f[w1][w2];
    }
};
