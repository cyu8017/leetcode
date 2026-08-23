// LeetCode 2824 - Count Pairs Whose Sum is Less than Target
// https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/

#include <vector>

class Solution {
public:
    int countPairs(std::vector<int>& nums, int target) {
        int ans = 0;
        for (int i = 0; i < (int)nums.size(); i++)
            for (int j = i + 1; j < (int)nums.size(); j++)
                if (nums[i] + nums[j] < target) ans++;
        return ans;
    }
};
