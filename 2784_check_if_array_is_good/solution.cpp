// LeetCode 2784 - Check if Array is Good
// https://leetcode.com/problems/check-if-array-is-good/

#include <vector>

class Solution {
public:
    bool isGood(std::vector<int>& nums) {
        int n = (int)nums.size() - 1;
        if (n < 1) return false;
        std::vector<int> freq(n + 1, 0);
        for (int v : nums) {
            if (v < 1 || v > n) return false;
            freq[v]++;
        }
        for (int i = 1; i < n; i++) if (freq[i] != 1) return false;
        return freq[n] == 2;
    }
};
