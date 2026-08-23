// LeetCode 0659 - Split Array into Consecutive Subsequences
// https://leetcode.com/problems/split-array-into-consecutive-subsequences/

#include <unordered_map>
#include <vector>

class Solution {
public:
    bool isPossible(std::vector<int>& nums) {
        std::unordered_map<int, int> freq;
        std::unordered_map<int, int> tails;
        for (int num : nums) {
            ++freq[num];
        }
        for (int num : nums) {
            if (freq[num] == 0) {
                continue;
            }
            --freq[num];
            if (tails[num - 1] > 0) {
                --tails[num - 1];
                ++tails[num];
            } else if (freq[num + 1] > 0 && freq[num + 2] > 0) {
                --freq[num + 1];
                --freq[num + 2];
                ++tails[num + 2];
            } else {
                return false;
            }
        }
        return true;
    }
};
