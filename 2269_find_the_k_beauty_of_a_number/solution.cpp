// LeetCode 2269 - Find the K-Beauty of a Number
// https://leetcode.com/problems/find-the-k-beauty-of-a-number/

#include <string>

class Solution {
public:
    int divisorSubstrings(int num, int k) {
        std::string s = std::to_string(num);
        int ans = 0;
        for (size_t i = 0; i + k <= s.size(); ++i) {
            int sub = 0;
            for (int j = 0; j < k; ++j) sub = sub * 10 + (s[i + j] - '0');
            if (sub != 0 && num % sub == 0) ans++;
        }
        return ans;
    }
};
