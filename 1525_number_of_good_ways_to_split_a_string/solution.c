// LeetCode 1525 - Number of Good Ways to Split a String
// https://leetcode.com/problems/number-of-good-ways-to-split-a-string/

#include <string.h>

int numSplits(char* s) {
    int right[26] = {0}, left[26] = {0};
    int n = (int)strlen(s);
    int rightDistinct = 0, leftDistinct = 0;
    for (int i = 0; i < n; i++) {
        if (right[s[i] - 'a']++ == 0) rightDistinct++;
    }
    int answer = 0;
    for (int i = 0; i < n - 1; i++) {
        int c = s[i] - 'a';
        if (left[c]++ == 0) leftDistinct++;
        if (--right[c] == 0) rightDistinct--;
        if (leftDistinct == rightDistinct) answer++;
    }
    return answer;
}
