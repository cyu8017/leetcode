// LeetCode 3171 - Find Subarray With Bitwise OR Closest to K
// https://leetcode.com/problems/find-subarray-with-bitwise-or-closest-to-k/

#include <vector>
#include <algorithm>
#include <cstdlib>
#include <climits>

class Solution {
public:
    int minimumDifference(std::vector<int>& nums, int k) {
        int mx = *std::max_element(nums.begin(), nums.end());
        int m = mx == 0 ? 1 : 32 - __builtin_clz(mx);
        std::vector<int> cnt(m);
        int ans = INT_MAX, s = 0, i = 0;
        for (int j = 0; j < (int)nums.size(); j++) {
            int x = nums[j];
            s |= x;
            ans = std::min(ans, std::abs(s - k));
            for (int h = 0; h < m; h++) if ((x >> h) & 1) cnt[h]++;
            while (i < j && s > k) {
                int y = nums[i];
                for (int h = 0; h < m; h++) {
                    if ((y >> h) & 1) {
                        if (--cnt[h] == 0) s ^= 1 << h;
                    }
                }
                ans = std::min(ans, std::abs(s - k));
                i++;
            }
        }
        return ans;
    }
};
