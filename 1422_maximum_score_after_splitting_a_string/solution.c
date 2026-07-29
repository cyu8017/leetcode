// LeetCode 1422 - Maximum Score After Splitting a String
// https://leetcode.com/problems/maximum-score-after-splitting-a-string/

#include <string.h>

int maxScore(char* s) {
    int ones = 0, n = (int)strlen(s);
    for (int i = 0; i < n; i++) if (s[i] == '1') ones++;
    int left_zeros = 0, answer = 0;
    for (int i = 0; i < n - 1; i++) {
        if (s[i] == '0') left_zeros++;
        else ones--;
        int score = left_zeros + ones;
        if (score > answer) answer = score;
    }
    return answer;
}
