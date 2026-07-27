// LeetCode 1064 - Fixed Point
// https://leetcode.com/problems/fixed-point/

#include <vector>

class Solution {
public:
    int fixedPoint(std::vector<int>& arr) {
        int lo = 0;
        int hi = static_cast<int>(arr.size()) - 1;
        int ans = -1;
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            if (arr[mid] == mid) {
                ans = mid;
                hi = mid - 1;
            } else if (arr[mid] < mid) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return ans;
    }
};
