// LeetCode 3357 - Minimize the Maximum Adjacent Element Difference
// https://leetcode.com/problems/minimize-the-maximum-adjacent-element-difference/

#include <cstdlib>
#include <vector>

class Solution {
public:
    int minDifference(std::vector<int>& nums) {
        int n = (int)nums.size();
        auto ok = [&](int d) {
            int prev = -1;
            for (int i = 0; i < n; i++) {
                if (nums[i] != -1) {
                    if (prev != -1 && std::abs(nums[i] - prev) > d) return false;
                    prev = nums[i];
                    continue;
                }
                int j = i;
                while (j < n && nums[j] == -1) j++;
                int left = prev;
                int right = (j < n) ? nums[j] : -1;
                int gap = j - i;
                if (left == -1 && right == -1) return true;
                if (left == -1 || right == -1) {
                    prev = -1;
                    i = j - 1;
                    continue;
                }
                if (std::abs(left - right) > d * (gap + 1)) return false;
                prev = -1;
                i = j - 1;
            }
            return true;
        };
        int lo = 0, hi = 1000000000;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (ok(mid)) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }
};
