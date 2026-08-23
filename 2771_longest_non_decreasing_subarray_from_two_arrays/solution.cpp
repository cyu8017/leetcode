// LeetCode 2771 - Longest Non-decreasing Subarray From Two Arrays
// https://leetcode.com/problems/longest-non-decreasing-subarray-from-two-arrays/

#include <algorithm>
#include <vector>

class Solution {
public:
    int maxNonDecreasingLength(std::vector<int>& nums1, std::vector<int>& nums2) {
        int n = (int)nums1.size();
        int dp1 = 1, dp2 = 1, ans = 1;
        for (int i = 1; i < n; i++) {
            int nd1 = 1, nd2 = 1;
            if (nums1[i] >= nums1[i - 1]) nd1 = std::max(nd1, dp1 + 1);
            if (nums1[i] >= nums2[i - 1]) nd1 = std::max(nd1, dp2 + 1);
            if (nums2[i] >= nums1[i - 1]) nd2 = std::max(nd2, dp1 + 1);
            if (nums2[i] >= nums2[i - 1]) nd2 = std::max(nd2, dp2 + 1);
            dp1 = nd1;
            dp2 = nd2;
            ans = std::max(ans, std::max(dp1, dp2));
        }
        return ans;
    }
};
