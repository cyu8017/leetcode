// LeetCode 3400 - Maximum Number of Matching Indices After Right Shifts
// https://leetcode.com/problems/maximum-number-of-matching-indices-after-right-shifts/

#include <vector>

class Solution {
public:
    int maximumMatchingIndices(std::vector<int>& nums1, std::vector<int>& nums2) {
        int n = (int)nums1.size();
        int ans = 0;
        for (int shift = 0; shift < n; shift++) {
            int cnt = 0;
            for (int i = 0; i < n; i++) {
                if (nums1[(i - shift + n) % n] == nums2[i]) cnt++;
            }
            if (cnt > ans) ans = cnt;
        }
        return ans;
    }
};
