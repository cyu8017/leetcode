// LeetCode 2870 - Minimum Number of Operations to Make Array Empty
// https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty/

#include <unordered_map>
#include <vector>

class Solution {
public:
    int minOperations(std::vector<int>& nums) {
        std::unordered_map<int, int> freq;
        for (int v : nums) freq[v]++;
        int ans = 0;
        for (auto& [_, c] : freq) {
            if (c == 1) return -1;
            ans += (c + 2) / 3;
        }
        return ans;
    }
};
