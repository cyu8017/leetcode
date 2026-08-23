// LeetCode 3843 - First Element With Unique Frequency
// https://leetcode.com/problems/first-element-with-unique-frequency/

#include <unordered_map>
#include <vector>

class Solution {
public:
    int firstUniqueFreq(std::vector<int>& nums) {
        std::unordered_map<int, int> cnt;
        for (int x : nums) cnt[x]++;
        std::unordered_map<int, int> freq;
        for (auto& [_, v] : cnt) freq[v]++;
        for (int x : nums) {
            if (freq[cnt[x]] == 1) return x;
        }
        return -1;
    }
};
