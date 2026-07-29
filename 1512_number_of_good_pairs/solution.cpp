// LeetCode 1512 - Number of Good Pairs
// https://leetcode.com/problems/number-of-good-pairs/

#include <unordered_map>
#include <vector>

class Solution {
public:
    int numIdenticalPairs(std::vector<int>& nums) {
        std::unordered_map<int, int> counts;
        for (int num : nums) {
            ++counts[num];
        }
        int answer = 0;
        for (const auto& [_, count] : counts) {
            answer += count * (count - 1) / 2;
        }
        return answer;
    }
};
