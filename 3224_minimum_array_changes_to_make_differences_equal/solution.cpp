// LeetCode 3224 - Minimum Array Changes to Make Differences Equal
// https://leetcode.com/problems/minimum-array-changes-to-make-differences-equal/

#include <vector>
#include <algorithm>

class Solution {
public:
    int minChanges(std::vector<int>& nums, int k) {
        std::vector<int> d(k + 2);
        int n = (int)nums.size();
        for (int i = 0; i < n / 2; i++) {
            int x = nums[i], y = nums[n - 1 - i];
            if (x > y) std::swap(x, y);
            d[0] += 1;
            d[y - x] -= 1;
            d[y - x + 1] += 1;
            int mx = std::max(y, k - x);
            d[mx + 1] -= 1;
            d[mx + 1] += 2;
        }
        int ans = n, s = 0;
        for (int x : d) {
            s += x;
            ans = std::min(ans, s);
        }
        return ans;
    }
};
