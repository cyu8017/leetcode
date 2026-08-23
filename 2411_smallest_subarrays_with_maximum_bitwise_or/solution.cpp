// LeetCode 2411 - Smallest Subarrays With Maximum Bitwise OR
// https://leetcode.com/problems/smallest-subarrays-with-maximum-bitwise-or/

#include <algorithm>
#include <vector>

class Solution {
public:
    std::vector<int> smallestSubarrays(std::vector<int>& nums) {
        int n = (int)nums.size();
        std::vector<int> ans(n);
        std::vector<int> last(32, -1);
        for (int i = n - 1; i >= 0; i--) {
            for (int b = 0; b < 32; b++) {
                if ((nums[i] >> b) & 1) last[b] = i;
            }
            int far = i;
            for (int b = 0; b < 32; b++) far = std::max(far, last[b]);
            ans[i] = far - i + 1;
        }
        return ans;
    }
};
