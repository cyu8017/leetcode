// LeetCode 1759 - Count Number of Homogenous Substrings
// https://leetcode.com/problems/count-number-of-homogenous-substrings/

#include <string>

class Solution {
public:
    int countHomogenous(std::string s) {
        const long long MOD = 1000000007LL;
        long long ans = 0;
        int n = (int)s.size();
        int i = 0;
        while (i < n) {
            int j = i;
            while (j < n && s[j] == s[i]) {
                j++;
            }
            long long length = j - i;
            ans = (ans + length * (length + 1) / 2) % MOD;
            i = j;
        }
        return (int)ans;
    }
};
