// LeetCode 3221 - Maximum Array Hopping Score II
// https://leetcode.com/problems/maximum-array-hopping-score-ii/

#include <vector>

class Solution {
public:
    long long maxScore(std::vector<int>& nums) {
        std::vector<int> stk;
        for (int i = 0; i < (int)nums.size(); i++) {
            while (!stk.empty() && nums[stk.back()] <= nums[i]) stk.pop_back();
            stk.push_back(i);
        }
        long long ans = 0;
        int i = 0;
        for (int j : stk) {
            ans += 1LL * (j - i) * nums[j];
            i = j;
        }
        return ans;
    }
};
