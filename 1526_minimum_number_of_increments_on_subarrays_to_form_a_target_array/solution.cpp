// LeetCode 1526 - Minimum Number of Increments on Subarrays to Form a Target Array
// https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/

#include <algorithm>
#include <vector>

class Solution {
public:
    int minNumberOperations(std::vector<int>& target) {
        int answer = target[0];
        for (std::size_t i = 1; i < target.size(); ++i) {
            answer += std::max(0, target[i] - target[i - 1]);
        }
        return answer;
    }
};
