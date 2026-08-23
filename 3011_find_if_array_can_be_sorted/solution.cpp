// LeetCode 3011 - Find if Array Can Be Sorted
// https://leetcode.com/problems/find-if-array-can-be-sorted/

#include <algorithm>
#include <vector>

class Solution {
public:
    bool canSortArray(std::vector<int>& nums) {
        int preMx = 0;
        int i = 0, n = (int)nums.size();
        while (i < n) {
            int cnt = __builtin_popcount((unsigned)nums[i]);
            int j = i + 1;
            int mi = nums[i], mx = nums[i];
            while (j < n && __builtin_popcount((unsigned)nums[j]) == cnt) {
                mi = std::min(mi, nums[j]);
                mx = std::max(mx, nums[j]);
                j++;
            }
            if (preMx > mi) return false;
            preMx = mx;
            i = j;
        }
        return true;
    }
};
