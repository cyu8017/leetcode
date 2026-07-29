// LeetCode 1936 - Add Minimum Number of Rungs
// https://leetcode.com/problems/add-minimum-number-of-rungs/

#include <vector>

class Solution {
public:
    int addRungs(std::vector<int>& rungs, int dist) {
        int prev = 0, ans = 0;
        for (int r : rungs) {
            int gap = r - prev;
            if (gap > dist) ans += (gap - 1) / dist;
            prev = r;
        }
        return ans;
    }
};
