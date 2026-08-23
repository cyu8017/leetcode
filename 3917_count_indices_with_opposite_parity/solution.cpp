// LeetCode 3917 - Count Indices With Opposite Parity
// https://leetcode.com/problems/count-indices-with-opposite-parity/

#include <vector>

class Solution {
public:
    std::vector<int> countOppositeParity(std::vector<int>& nums) {
        int cnt[2] = {0, 0};
        for (int x : nums) cnt[x & 1]++;
        int n = (int)nums.size();
        std::vector<int> ans(n);
        for (int i = 0; i < n; i++) {
            int x = nums[i];
            cnt[x & 1]--;
            ans[i] = cnt[(x & 1) ^ 1];
        }
        return ans;
    }
};
