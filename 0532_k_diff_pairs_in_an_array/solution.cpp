// LeetCode 0532 - K-diff Pairs in an Array
// https://leetcode.com/problems/k-diff-pairs-in-an-array/

#include <unordered_map>
#include <vector>

class Solution {
public:
    int findPairs(std::vector<int>& nums, int k) {
        if (k < 0) {
            return 0;
        }

        std::unordered_map<int, int> freq;
        for (const int num : nums) {
            ++freq[num];
        }

        int pairs = 0;
        for (const auto& entry : freq) {
            const int num = entry.first;
            if (k == 0) {
                if (entry.second > 1) {
                    ++pairs;
                }
            } else if (freq.count(num + k)) {
                ++pairs;
            }
        }
        return pairs;
    }
};
