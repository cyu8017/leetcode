// LeetCode 2376 - Count Special Integers
// https://leetcode.com/problems/count-special-integers/

#include <string>

class Solution {
public:
    int countSpecialNumbers(int n) {
        std::string s = std::to_string(n);
        int m = (int)s.size();
        int ans = 0;
        int perm = 9;
        for (int i = 1; i < m; i++) {
            ans += perm;
            perm *= (10 - i);
        }
        bool used[10] = {};
        for (int i = 0; i < m; i++) {
            int start = i == 0 ? 1 : 0;
            int digit = s[i] - '0';
            for (int d = start; d < digit; d++) {
                if (used[d]) continue;
                int rem = 10 - (i + 1);
                int ways = 1;
                for (int j = i + 1; j < m; j++) {
                    ways *= rem;
                    rem--;
                }
                ans += ways;
            }
            if (used[digit]) return ans;
            used[digit] = true;
        }
        return ans + 1;
    }
};
