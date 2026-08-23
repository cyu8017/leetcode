// LeetCode 2541 - Minimum Operations to Make Array Equal II
// https://leetcode.com/problems/minimum-operations-to-make-array-equal-ii/

#include <vector>

class Solution {
public:
    long long minOperations(std::vector<int>& nums1, std::vector<int>& nums2, int k) {
        if (k == 0) {
            for (int i = 0; i < (int)nums1.size(); i++) {
                if (nums1[i] != nums2[i]) return -1;
            }
            return 0;
        }
        long long pos = 0, neg = 0;
        for (int i = 0; i < (int)nums1.size(); i++) {
            int d = nums1[i] - nums2[i];
            if (d % k != 0) return -1;
            if (d > 0) pos += d / k;
            else neg += (-d) / k;
        }
        return pos != neg ? -1 : pos;
    }
};
