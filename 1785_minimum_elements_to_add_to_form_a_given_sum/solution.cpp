// LeetCode 1785 - Minimum Elements to Add to Form a Given Sum
// https://leetcode.com/problems/minimum-elements-to-add-to-form-a-given-sum/

#include <cstdlib>
#include <vector>

class Solution {
public:
    int minElements(std::vector<int>& nums, int limit, int goal) {
        long long sum = 0;
        for (int num : nums) {
            sum += num;
        }
        long long diff = std::llabs(sum - goal);
        return (int)((diff + limit - 1) / limit);
    }
};
