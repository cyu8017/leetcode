// LeetCode 3404 - Count Special Subsequences
// https://leetcode.com/problems/count-special-subsequences/

#include <cstdint>
#include <vector>

class Solution {
public:
    long long numberOfSubsequences(std::vector<int>& nums) {
        int n = (int)nums.size();
        long long ans = 0;
        for (int i = 0; i < n; i++) {
            for (int j = i + 2; j < n; j++) {
                for (int k = j + 2; k < n; k++) {
                    for (int l = k + 2; l < n; l++) {
                        if ((long long)nums[i] * nums[k] == (long long)nums[j] * nums[l]) ans++;
                    }
                }
            }
        }
        return ans;
    }
};
