// LeetCode 1593 - Split a String Into the Max Number of Unique Substrings
// https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings/

#include <stdlib.h>
#include <string.h>

static int answer1593;
static char** used1593;
static int usedSize1593;

static int contains1593(const char* part) {
    for (int i = 0; i < usedSize1593; i++) if (strcmp(used1593[i], part) == 0) return 1;
    return 0;
}

static void dfs1593(const char* s, int n, int i) {
    if (usedSize1593 + n - i <= answer1593) return;
    if (i == n) {
        if (usedSize1593 > answer1593) answer1593 = usedSize1593;
        return;
    }
    for (int j = i + 1; j <= n; j++) {
        int len = j - i;
        char* part = (char*)malloc((size_t)len + 1);
        memcpy(part, s + i, (size_t)len);
        part[len] = '\0';
        if (!contains1593(part)) {
            used1593[usedSize1593++] = part;
            dfs1593(s, n, j);
            free(used1593[--usedSize1593]);
        } else {
            free(part);
        }
    }
}

int maxUniqueSplit(char* s) {
    int n = (int)strlen(s);
    answer1593 = 0;
    usedSize1593 = 0;
    used1593 = (char**)malloc((size_t)n * sizeof(char*));
    dfs1593(s, n, 0);
    free(used1593);
    return answer1593;
}
