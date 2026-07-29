// LeetCode 1177 - Can Make Palindrome from Substring
// https://leetcode.com/problems/can-make-palindrome-from-substring/

#include <string>
#include <vector>

class Solution {
public:
    std::vector<bool> canMakePaliQueries(std::string s, std::vector<std::vector<int>>& queries) {
        std::vector<int> prefix(1, 0);
        int mask = 0;
        for (char ch : s) {
            mask ^= 1 << (ch - 'a');
            prefix.push_back(mask);
        }
        std::vector<bool> ans;
        for (const auto& q : queries) {
            int bits = __builtin_popcount(prefix[q[1] + 1] ^ prefix[q[0]]);
            ans.push_back(bits / 2 <= q[2]);
        }
        return ans;
    }
};
