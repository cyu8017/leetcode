// LeetCode 1147 - Longest Chunked Palindrome Decomposition
// https://leetcode.com/problems/longest-chunked-palindrome-decomposition/

#include <string>

class Solution {
public:
    int longestDecomposition(std::string text) {
        int n = static_cast<int>(text.size()), ans = 0, i = 0;
        while (i < n - i) {
            bool found = false;
            for (int length = 1; length <= (n - 2 * i) / 2; ++length) {
                if (text.substr(i, length) == text.substr(n - i - length, length)) {
                    ans += 2;
                    i += length;
                    found = true;
                    break;
                }
            }
            if (!found) { ans += 1; break; }
        }
        return ans;
    }
};
