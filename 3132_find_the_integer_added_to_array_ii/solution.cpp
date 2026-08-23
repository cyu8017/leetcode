// LeetCode 3132 - Find the Integer Added to Array II
// https://leetcode.com/problems/find-the-integer-added-to-array-ii/

#include <vector>
#include <algorithm>

class Solution {
public:
    int minimumAddedInteger(std::vector<int>& nums1, std::vector<int>& nums2) {
        std::sort(nums1.begin(), nums1.end());
        std::sort(nums2.begin(), nums2.end());
        int ans = 1 << 30;
        auto f = [&](int x) {
            int i = 0, j = 0, cnt = 0;
            while (i < (int)nums1.size() && j < (int)nums2.size()) {
                if (nums2[j] - nums1[i] != x) cnt++;
                else j++;
                i++;
            }
            return cnt <= 2;
        };
        for (int t = 0; t < 3; t++) {
            int x = nums2[0] - nums1[t];
            if (f(x)) ans = std::min(ans, x);
        }
        return ans;
    }
};
