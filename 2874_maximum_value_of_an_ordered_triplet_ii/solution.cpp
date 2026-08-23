// LeetCode 2874 - Maximum Value of an Ordered Triplet II
// https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-ii/

#include <vector>

class Solution {
public:
    long long maximumTripletValue(std::vector<int>& nums) {
        long long ans = 0, maxI = 0, maxDiff = 0;
        for (int v : nums) {
            long long val = v;
            if (maxDiff * val > ans) ans = maxDiff * val;
            if (maxI - val > maxDiff) maxDiff = maxI - val;
            if (val > maxI) maxI = val;
        }
        return ans;
    }
};
