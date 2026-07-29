// LeetCode 0985 - Sum of Even Numbers After Queries
// https://leetcode.com/problems/sum-of-even-numbers-after-queries/

#include <vector>

class Solution {
public:
    std::vector<int> sumEvenAfterQueries(std::vector<int>& nums, std::vector<std::vector<int>>& queries) {
        int even = 0;
        for (int x : nums) if (x % 2 == 0) even += x;
        std::vector<int> ans;
        for (auto& q : queries) {
            int val = q[0], i = q[1];
            if (nums[i] % 2 == 0) even -= nums[i];
            nums[i] += val;
            if (nums[i] % 2 == 0) even += nums[i];
            ans.push_back(even);
        }
        return ans;
    }
};
