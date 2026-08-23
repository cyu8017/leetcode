// LeetCode 3595 - Once Twice
// https://leetcode.com/problems/once-twice/

#include <unordered_map>
#include <vector>

class Solution {
public:
    std::vector<int> onceTwice(std::vector<int>& nums) {
        std::unordered_map<int, int> freq;
        for (int x : nums) freq[x]++;
        int a = 0, b = 0;
        for (auto& [x, c] : freq) {
            if (c == 1) a = x;
            else if (c == 2) b = x;
        }
        return {a, b};
    }
};
