// LeetCode 1186 - Maximum Subarray Sum with One Deletion
// https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/

#include <algorithm>
#include <vector>

class Solution {
public:
    int maximumSum(std::vector<int>& arr) {
        int keep = arr[0], del = arr[0], ans = arr[0];
        for (int i = 1; i < static_cast<int>(arr.size()); ++i) {
            int x = arr[i];
            del = std::max(keep, del + x);
            keep = std::max(keep + x, x);
            ans = std::max({ans, keep, del});
        }
        return ans;
    }
};
