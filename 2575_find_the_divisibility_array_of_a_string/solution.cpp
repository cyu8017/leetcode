// LeetCode 2575 - Find the Divisibility Array of a String
// https://leetcode.com/problems/find-the-divisibility-array-of-a-string/

#include <string>
#include <vector>

class Solution {
public:
    std::vector<int> divisibilityArray(std::string word, int m) {
        std::vector<int> ans(word.size());
        long long cur = 0;
        for (size_t i = 0; i < word.size(); ++i) {
            cur = (cur * 10 + (word[i] - '0')) % m;
            if (cur == 0) ans[i] = 1;
        }
        return ans;
    }
};
