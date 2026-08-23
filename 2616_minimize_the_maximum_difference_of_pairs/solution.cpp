// LeetCode 2616 - Minimize the Maximum Difference of Pairs
// https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/

#include <algorithm>
#include <vector>

class Solution {
public:
    int minimizeMax(std::vector<int>& nums, int p) {
        std::sort(nums.begin(), nums.end());
        auto ok = [&](int d) {
            int cnt = 0;
            for (int i = 0; i + 1 < (int)nums.size();) {
                if (nums[i + 1] - nums[i] <= d) {
                    cnt++;
                    i += 2;
                } else {
                    i++;
                }
            }
            return cnt >= p;
        };
        int lo = 0, hi = nums.back() - nums.front();
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (ok(mid)) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }
};
