// LeetCode 1152 - Analyze User Website Visit Pattern
// https://leetcode.com/problems/analyze-user-website-visit-pattern/

#include <stdlib.h>
#include <string.h>
#include <stdio.h>

typedef struct { char* user; int time; char* site; } Visit;
typedef struct { char a[22]; char b[22]; char c[22]; int count; } Pattern;

static int cmpVisit(const void* x, const void* y) {
    const Visit* a = (const Visit*)x;
    const Visit* b = (const Visit*)y;
    int cu = strcmp(a->user, b->user);
    if (cu) return cu;
    return a->time - b->time;
}

static int cmpPat(const void* x, const void* y) {
    const Pattern* a = (const Pattern*)x;
    const Pattern* b = (const Pattern*)y;
    if (a->count != b->count) return b->count - a->count;
    int c1 = strcmp(a->a, b->a); if (c1) return c1;
    int c2 = strcmp(a->b, b->b); if (c2) return c2;
    return strcmp(a->c, b->c);
}

char** mostVisitedPattern(char** username, int usernameSize, int* timestamp, int timestampSize, char** website, int websiteSize, int* returnSize) {
    (void)timestampSize; (void)websiteSize;
    Visit* visits = (Visit*)malloc((size_t)usernameSize * sizeof(Visit));
    for (int i = 0; i < usernameSize; i++) {
        visits[i].user = username[i];
        visits[i].time = timestamp[i];
        visits[i].site = website[i];
    }
    qsort(visits, (size_t)usernameSize, sizeof(Visit), cmpVisit);

    Pattern* pats = (Pattern*)calloc(5000, sizeof(Pattern));
    int pcount = 0;

    int i = 0;
    while (i < usernameSize) {
        int j = i;
        while (j < usernameSize && strcmp(visits[j].user, visits[i].user) == 0) j++;
        int m = j - i;
        char seen[500][66];
        int seenN = 0;
        for (int a = 0; a < m; a++) {
            for (int b = a + 1; b < m; b++) {
                for (int c = b + 1; c < m; c++) {
                    char key[66];
                    snprintf(key, sizeof(key), "%s|%s|%s", visits[i + a].site, visits[i + b].site, visits[i + c].site);
                    int dup = 0;
                    for (int s = 0; s < seenN; s++) if (strcmp(seen[s], key) == 0) { dup = 1; break; }
                    if (dup) continue;
                    strcpy(seen[seenN++], key);
                    int found = -1;
                    for (int p = 0; p < pcount; p++) {
                        if (strcmp(pats[p].a, visits[i + a].site) == 0 &&
                            strcmp(pats[p].b, visits[i + b].site) == 0 &&
                            strcmp(pats[p].c, visits[i + c].site) == 0) { found = p; break; }
                    }
                    if (found >= 0) pats[found].count++;
                    else {
                        strcpy(pats[pcount].a, visits[i + a].site);
                        strcpy(pats[pcount].b, visits[i + b].site);
                        strcpy(pats[pcount].c, visits[i + c].site);
                        pats[pcount].count = 1;
                        pcount++;
                    }
                }
            }
        }
        i = j;
    }
    qsort(pats, (size_t)pcount, sizeof(Pattern), cmpPat);
    char** ans = (char**)malloc(3 * sizeof(char*));
    ans[0] = (char*)malloc(strlen(pats[0].a) + 1); strcpy(ans[0], pats[0].a);
    ans[1] = (char*)malloc(strlen(pats[0].b) + 1); strcpy(ans[1], pats[0].b);
    ans[2] = (char*)malloc(strlen(pats[0].c) + 1); strcpy(ans[2], pats[0].c);
    *returnSize = 3;
    free(visits); free(pats);
    return ans;
}
