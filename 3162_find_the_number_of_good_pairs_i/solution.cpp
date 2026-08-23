// LeetCode 3162 - Find the Number of Good Pairs I
// https://leetcode.com/problems/find-the-number-of-good-pairs-i/

#include <vector>

class Solution {
public:
    int numberOfPairs(std::vector<int>& nums1, std::vector<int>& nums2, int k) {
        int ans = 0;
        for (int x : nums1)
            for (int y : nums2)
                if (x % (y * k) == 0) ans++;
        return ans;
    }
};
