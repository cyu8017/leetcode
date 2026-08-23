// LeetCode 3231 - Minimum Number of Increasing Subsequence to Be Removed
// https://leetcode.com/problems/minimum-number-of-increasing-subsequence-to-be-removed/

#include <vector>

class Solution {
public:
    int minOperations(std::vector<int>& nums) {
        std::vector<int> g;
        for (int x : nums) {
            int l = 0, r = (int)g.size();
            while (l < r) {
                int mid = (l + r) >> 1;
                if (g[mid] < x) r = mid;
                else l = mid + 1;
            }
            if (l == (int)g.size()) g.push_back(x);
            else g[l] = x;
        }
        return (int)g.size();
    }
};
