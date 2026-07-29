// LeetCode 1446 - Consecutive Characters
// https://leetcode.com/problems/consecutive-characters/

#include <string.h>

int maxPower(char* s) {
    int answer = 1, run = 1;
    for (int i = 1; s[i]; i++) {
        run = s[i] == s[i - 1] ? run + 1 : 1;
        if (run > answer) answer = run;
    }
    return answer;
}
