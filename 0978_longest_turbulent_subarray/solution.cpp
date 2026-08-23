// LeetCode 0978 - Longest Turbulent Subarray
// https://leetcode.com/problems/longest-turbulent-subarray/

#include <algorithm>
#include <vector>

class Solution {
public:
    int maxTurbulenceSize(std::vector<int>& arr) {
        int ans = 1, cur = 1;
        for (int i = 1; i < (int)arr.size(); i++) {
            if (arr[i] == arr[i - 1]) cur = 1;
            else if (i == 1 || (arr[i] - arr[i - 1]) * 1LL * (arr[i - 1] - arr[i - 2]) < 0) cur++;
            else cur = 2;
            ans = std::max(ans, cur);
        }
        return ans;
    }
};
