// LeetCode 2272 - Substring With Largest Variance
// https://leetcode.com/problems/substring-with-largest-variance/

#include <string.h>

int largestVariance(char* s) {
    int ans = 0;
    int n = (int)strlen(s);
    for (char a = 'a'; a <= 'z'; a++) {
        for (char b = 'a'; b <= 'z'; b++) {
            if (a == b) continue;
            int bal = 0;
            int hasB = 0;
            for (int i = 0; i < n; i++) {
                if (s[i] == a) bal++;
                else if (s[i] == b) { bal--; hasB = 1; }
                if (hasB && bal > ans) ans = bal;
                if (bal < 0) { bal = 0; hasB = 0; }
            }
        }
    }
    return ans;
}
