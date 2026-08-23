// LeetCode 0906 - Super Palindromes
// https://leetcode.com/problems/super-palindromes/

#include <algorithm>
#include <string>

class Solution {
public:
    int superpalindromesInRange(std::string left, std::string right) {
        long long L = std::stoll(left), R = std::stoll(right);
        int ans = 0;

        auto isPal = [](long long x) {
            std::string s = std::to_string(x);
            int n = (int)s.size();
            for (int i = 0; i < n / 2; i++) {
                if (s[i] != s[n - 1 - i]) return false;
            }
            return true;
        };

        for (long long k = 1; k <= 100000; k++) {
            std::string s = std::to_string(k);
            std::string rev = s;
            std::reverse(rev.begin(), rev.end());
            long long pal = std::stoll(s + rev);
            long long sq = pal * pal;
            if (sq > R) break;
            if (sq >= L && isPal(sq)) ans++;
        }
        for (long long k = 1; k <= 100000; k++) {
            std::string s = std::to_string(k);
            std::string rev = s.substr(0, s.size() - 1);
            std::reverse(rev.begin(), rev.end());
            long long pal = std::stoll(s + rev);
            long long sq = pal * pal;
            if (sq > R) break;
            if (sq >= L && isPal(sq)) ans++;
        }
        return ans;
    }
};
