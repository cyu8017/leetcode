// LeetCode 3333 - Find the Original Typed String II
// https://leetcode.com/problems/find-the-original-typed-string-ii/

#include <string>
#include <vector>

class Solution {
public:
    int possibleStringCount(std::string word, int k) {
        const int mod = 1000000007;
        std::vector<int> groups;
        for (int i = 0; i < (int)word.size(); ) {
            int j = i;
            while (j < (int)word.size() && word[j] == word[i]) j++;
            groups.push_back(j - i);
            i = j;
        }
        int total = 1;
        for (int g : groups) total = (int)((long long)total * g % mod);
        if (k <= (int)groups.size()) return total;
        int need = k - 1;
        std::vector<int> dp(need, 0);
        dp[0] = 1;
        for (int g : groups) {
            std::vector<int> ndp(need, 0);
            std::vector<int> pref(need + 1, 0);
            for (int i = 0; i < need; i++) pref[i + 1] = (pref[i] + dp[i]) % mod;
            for (int s = 0; s < need; s++) {
                int lo = s - g;
                if (lo < 0) lo = 0;
                int hi = s - 1;
                if (hi >= 0) ndp[s] = (pref[hi + 1] - pref[lo] + mod) % mod;
            }
            dp = ndp;
        }
        int bad = 0;
        for (int v : dp) bad = (bad + v) % mod;
        return (total - bad + mod) % mod;
    }
};
