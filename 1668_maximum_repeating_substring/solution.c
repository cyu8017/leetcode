// LeetCode 1668 - Maximum Repeating Substring
// https://leetcode.com/problems/maximum-repeating-substring/

#include <stdlib.h>
#include <string.h>

int maxRepeating(char* sequence, char* word) {
    int sl = (int)strlen(sequence), wl = (int)strlen(word);
    if (wl == 0) return 0;
    int maxK = sl / wl;
    char* buf = (char*)malloc((size_t)sl + 1);
    int k = 0;
    for (int t = 1; t <= maxK; t++) {
        buf[0] = '\0';
        for (int i = 0; i < t; i++) strcat(buf, word);
        if (strstr(sequence, buf)) k = t;
        else break;
    }
    free(buf);
    return k;
}
