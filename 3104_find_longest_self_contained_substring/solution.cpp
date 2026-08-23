// LeetCode 3104 - Find Longest Self-Contained Substring
// https://leetcode.com/problems/find-longest-self-contained-substring/

#include <algorithm>
#include <string>

class Solution {
public:
    int maxSubstringLength(std::string s) {
        int first[26], last[26];
        for (int i = 0; i < 26; i++) first[i] = -1;
        int n = (int)s.size();
        for (int i = 0; i < n; i++) {
            int j = s[i] - 'a';
            if (first[j] == -1) first[j] = i;
            last[j] = i;
        }
        int ans = -1;
        for (int k = 0; k < 26; k++) {
            int i = first[k];
            if (i == -1) continue;
            int mx = last[k];
            for (int j = i; j < n; j++) {
                int a = first[s[j] - 'a'], b = last[s[j] - 'a'];
                if (a < i) break;
                mx = std::max(mx, b);
                if (mx == j && j - i + 1 < n) ans = std::max(ans, j - i + 1);
            }
        }
        return ans;
    }
};
