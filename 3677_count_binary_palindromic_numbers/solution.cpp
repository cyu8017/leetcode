// LeetCode 3677 - Count Binary Palindromic Numbers
// https://leetcode.com/problems/count-binary-palindromic-numbers/

#include <algorithm>
#include <string>

class Solution {
public:
    int countBinaryPalindromes(long long n) {
        if (n == 0) return 1;
        int ans = 1;
        std::string s;
        {
            long long x = n;
            while (x > 0) {
                s.push_back(char('0' + (x & 1)));
                x >>= 1;
            }
            std::reverse(s.begin(), s.end());
        }
        int L = (int)s.size();
        for (int len_ = 1; len_ < L; len_++) {
            int half = (len_ + 1) / 2;
            ans += 1 << (half - 1);
        }
        int half = (L + 1) / 2;
        std::string prefix = s.substr(0, half);
        int start = 1 << (half - 1);
        long long prefVal = 0;
        for (char c : prefix) prefVal = (prefVal << 1) | (c - '0');
        ans += (int)prefVal - start;
        std::string pal = prefix;
        for (int i = half - 1 - (L % 2); i >= 0; i--) pal.push_back(prefix[i]);
        long long pval = 0;
        for (char c : pal) pval = (pval << 1) | (c - '0');
        if (pval <= n) ans++;
        return ans;
    }
};
