// LeetCode 3412 - Find Mirror Score of a String
// https://leetcode.com/problems/find-mirror-score-of-a-string/

#include <stdlib.h>
#include <string.h>

long long calculateScore(char* s) {
    int n = (int)strlen(s);
    int* stacks[26];
    int top[26] = {0}, cap[26];
    for (int i = 0; i < 26; i++) { cap[i] = 8; stacks[i] = (int*)malloc(8 * sizeof(int)); }
    long long ans = 0;
    for (int i = 0; i < n; i++) {
        int ci = s[i] - 'a', mir = 25 - ci;
        if (top[mir] > 0) {
            int j = stacks[mir][--top[mir]];
            ans += i - j;
        } else {
            if (top[ci] == cap[ci]) { cap[ci] *= 2; stacks[ci] = (int*)realloc(stacks[ci], cap[ci] * sizeof(int)); }
            stacks[ci][top[ci]++] = i;
        }
    }
    for (int i = 0; i < 26; i++) free(stacks[i]);
    return ans;
}
