// LeetCode 3029 - Minimum Time to Revert Word to Initial State I
// https://leetcode.com/problems/minimum-time-to-revert-word-to-initial-state-i/

#include <string>

class Solution {
public:
    int minimumTimeToInitialState(std::string word, int k) {
        int n = (int)word.size();
        for (int i = k; i < n; i += k)
            if (word.substr(i) == word.substr(0, n - i)) return i / k;
        return (n + k - 1) / k;
    }
};
