// LeetCode 2800 - Shortest String That Contains Three Strings
// https://leetcode.com/problems/shortest-string-that-contains-three-strings/

#include <stdlib.h>
#include <string.h>
#include <stdio.h>

static int contains(const char* x, const char* y) {
    return strstr(x, y) != NULL;
}

static char* merge(const char* x, const char* y) {
    if (contains(x, y)) {
        char* r = (char*)malloc(strlen(x) + 1);
        strcpy(r, x);
        return r;
    }
    int lx = (int)strlen(x), ly = (int)strlen(y);
    char* best = (char*)malloc(lx + ly + 1);
    strcpy(best, x); strcat(best, y);
    int n = lx < ly ? lx : ly;
    for (int i = n; i > 0; i--) {
        if (strncmp(x + lx - i, y, i) == 0) {
            char* cand = (char*)malloc(lx + ly - i + 1);
            memcpy(cand, x, lx);
            strcpy(cand + lx, y + i);
            if ((int)strlen(cand) < (int)strlen(best) ||
                ((int)strlen(cand) == (int)strlen(best) && strcmp(cand, best) < 0)) {
                free(best); best = cand;
            } else free(cand);
            break;
        }
    }
    return best;
}

char* minimumString(char* a, char* b, char* c) {
    char* perms[6][3] = {
        {a,b,c},{a,c,b},{b,a,c},{b,c,a},{c,a,b},{c,b,a}
    };
    char* ans = NULL;
    for (int i = 0; i < 6; i++) {
        char* m1 = merge(perms[i][0], perms[i][1]);
        char* cur = merge(m1, perms[i][2]);
        free(m1);
        if (!ans || (int)strlen(cur) < (int)strlen(ans) ||
            ((int)strlen(cur) == (int)strlen(ans) && strcmp(cur, ans) < 0)) {
            free(ans); ans = cur;
        } else free(cur);
    }
    return ans;
}
