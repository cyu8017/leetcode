// LeetCode 3969 - Valid Subarrays With Matching Sum Digits I
// https://leetcode.com/problems/valid-subarrays-with-matching-sum-digits-i/

#include <string>
#include <vector>

class Solution {
public:
    int countValidSubarrays(std::vector<int>& nums, int x) {
        int n = (int)nums.size();
        int ans = 0;
        for (int l = 0; l < n; l++) {
            long long s = 0;
            for (int r = l; r < n; r++) {
                s += nums[r];
                if (s % 10 == x) {
                    std::string t = std::to_string(s);
                    if (t[0] - '0' == x) ans++;
                }
            }
        }
        return ans;
    }
};
