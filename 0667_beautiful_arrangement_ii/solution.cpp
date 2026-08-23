// LeetCode 0667 - Beautiful Arrangement II
// https://leetcode.com/problems/beautiful-arrangement-ii/

#include <vector>

class Solution {
public:
    std::vector<int> constructArray(int n, int k) {
        std::vector<int> res;
        for (int i = 1; i <= n - k; ++i) {
            res.push_back(i);
        }
        int left = n - k + 1;
        int right = n;
        bool takeHigh = true;
        while (left <= right) {
            if (takeHigh) {
                res.push_back(right--);
            } else {
                res.push_back(left++);
            }
            takeHigh = !takeHigh;
        }
        return res;
    }
};
