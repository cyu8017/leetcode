// LeetCode 3685 - Subsequence Sum After Capping Elements
// https://leetcode.com/problems/subsequence-sum-after-capping-elements/

#include <algorithm>
#include <vector>

class Solution {
public:
    std::vector<bool> subsequenceSumAfterCapping(std::vector<int>& nums, int k) {
        int n = (int)nums.size();
        std::vector<int> sorted = nums;
        std::sort(sorted.begin(), sorted.end());
        std::vector<bool> ans(n), reach(k + 1, false);
        reach[0] = true;
        int idx = 0;
        for (int x = 1; x <= n; x++) {
            while (idx < n && sorted[idx] <= x) {
                int v = sorted[idx];
                for (int s = k; s >= v; s--) {
                    if (reach[s - v]) reach[s] = true;
                }
                idx++;
            }
            std::vector<bool> tmp = reach;
            int rem = n - idx;
            for (int s = 0; s <= k; s++) {
                if (!reach[s]) continue;
                for (int t = 1; t <= rem && s + t * x <= k; t++) tmp[s + t * x] = true;
            }
            ans[x - 1] = tmp[k];
        }
        return ans;
    }
};
