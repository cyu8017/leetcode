// LeetCode 0330 - Patching Array
// https://leetcode.com/problems/patching-array/

#include <vector>

class Solution {
public:
    int minPatches(std::vector<int>& nums, int n) {
        int patches = 0;
        long long miss = 1;
        int index = 0;
        while (miss <= n) {
            if (index < static_cast<int>(nums.size()) && nums[index] <= miss) {
                miss += nums[index];
                index += 1;
            } else {
                miss += miss;
                patches += 1;
            }
        }
        return patches;
    }
};
