// LeetCode 2420 - Find All Good Indices
// https://leetcode.com/problems/find-all-good-indices/

#include <vector>

class Solution {
public:
    std::vector<int> goodIndices(std::vector<int>& nums, int k) {
        int n = (int)nums.size();
        std::vector<int> dec(n), inc(n);
        dec[0] = 1;
        for (int i = 1; i < n; i++) {
            dec[i] = nums[i] <= nums[i - 1] ? dec[i - 1] + 1 : 1;
        }
        inc[n - 1] = 1;
        for (int i = n - 2; i >= 0; i--) {
            inc[i] = nums[i] <= nums[i + 1] ? inc[i + 1] + 1 : 1;
        }
        std::vector<int> ans;
        for (int i = k; i < n - k; i++) {
            if (dec[i - 1] >= k && inc[i + 1] >= k) ans.push_back(i);
        }
        return ans;
    }
};
