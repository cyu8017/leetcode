// LeetCode 1888 - Minimum Number of Flips to Make the Binary String Alternating
// https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/

#include <string.h>

int minFlips(char* s) {
    int n = (int)strlen(s);
    int alt0 = 0, alt1 = 0;
    for (int i = 0; i < n; i++) {
        char expect0 = (i % 2 == 0) ? '0' : '1';
        char expect1 = (i % 2 == 0) ? '1' : '0';
        if (s[i] != expect0) alt0++;
        if (s[i] != expect1) alt1++;
    }
    int answer = alt0 < alt1 ? alt0 : alt1;
    for (int i = 0; i < n; i++) {
        char leave0 = (i % 2 == 0) ? '0' : '1';
        char leave1 = (i % 2 == 0) ? '1' : '0';
        if (s[i] != leave0) alt0--;
        if (s[i] != leave1) alt1--;
        int j = i + n;
        char enter0 = (j % 2 == 0) ? '0' : '1';
        char enter1 = (j % 2 == 0) ? '1' : '0';
        if (s[i] != enter0) alt0++;
        if (s[i] != enter1) alt1++;
        if (alt0 < answer) answer = alt0;
        if (alt1 < answer) answer = alt1;
    }
    return answer;
}
