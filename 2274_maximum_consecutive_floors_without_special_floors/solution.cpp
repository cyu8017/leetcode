// LeetCode 2274 - Maximum Consecutive Floors Without Special Floors
// https://leetcode.com/problems/maximum-consecutive-floors-without-special-floors/

#include <vector>
#include <algorithm>

class Solution {
public:
    int maxConsecutive(int bottom, int top, std::vector<int>& special) {
        std::sort(special.begin(), special.end());
        int ans = special[0] - bottom;
        for (size_t i = 1; i < special.size(); ++i)
            ans = std::max(ans, special[i] - special[i - 1] - 1);
        ans = std::max(ans, top - special.back());
        return ans;
    }
};
