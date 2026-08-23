// LeetCode 3046 - Split the Array
// https://leetcode.com/problems/split-the-array/

#include <vector>

class Solution {
public:
    bool isPossibleToSplit(std::vector<int>& nums) {
        int cnt[101] = {};
        for (int x : nums) {
            cnt[x]++;
            if (cnt[x] >= 3) return false;
        }
        return true;
    }
};
