// LeetCode 3097 - Shortest Subarray With OR at Least K II
// https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-ii/

#include <algorithm>
#include <vector>

class Solution {
public:
    int minimumSubarrayLength(std::vector<int>& nums, int k) {
        int n = (int)nums.size();
        int cnt[32] = {};
        int ans = n + 1, s = 0, i = 0;
        for (int j = 0; j < n; j++) {
            int x = nums[j];
            s |= x;
            for (int h = 0; h < 32; h++)
                if ((x >> h) & 1) cnt[h]++;
            for (; s >= k && i <= j; i++) {
                ans = std::min(ans, j - i + 1);
                for (int h = 0; h < 32; h++) {
                    if ((nums[i] >> h) & 1) {
                        cnt[h]--;
                        if (cnt[h] == 0) s ^= 1 << h;
                    }
                }
            }
        }
        return ans == n + 1 ? -1 : ans;
    }
};
