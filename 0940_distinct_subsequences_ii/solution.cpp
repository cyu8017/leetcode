// LeetCode 0940 - Distinct Subsequences II
// https://leetcode.com/problems/distinct-subsequences-ii/

#include <string>

class Solution {
public:
    int distinctSubseqII(std::string s) {
        const int MOD = 1000000007;
        long long ends[26] = {};
        long long total = 1;
        for (char ch : s) {
            long long prev = ends[ch - 'a'];
            ends[ch - 'a'] = total;
            total = (total - prev + ends[ch - 'a'] + MOD) % MOD;
        }
        return (int)((total - 1 + MOD) % MOD);
    }
};
