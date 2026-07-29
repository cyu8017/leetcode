// LeetCode 0884 - Uncommon Words from Two Sentences
// https://leetcode.com/problems/uncommon-words-from-two-sentences/

#include <stdlib.h>
#include <string.h>
#include <stdio.h>

char** uncommonFromSentences(char* s1, char* s2, int* returnSize) {
    char buf[400];
    snprintf(buf, sizeof(buf), "%s %s", s1, s2);
    typedef struct { char w[40]; int c; } Ent;
    Ent ents[200];
    int nent = 0;
    char* copy = (char*)malloc(strlen(buf) + 1);
    strcpy(copy, buf);
    for (char* tok = strtok(copy, " "); tok; tok = strtok(NULL, " ")) {
        int found = -1;
        for (int i = 0; i < nent; i++) if (strcmp(ents[i].w, tok) == 0) { found = i; break; }
        if (found >= 0) ents[found].c++;
        else { strcpy(ents[nent].w, tok); ents[nent].c = 1; nent++; }
    }
    free(copy);
    char** ans = (char**)malloc((size_t)nent * sizeof(char*));
    int count = 0;
    for (int i = 0; i < nent; i++) if (ents[i].c == 1) {
        ans[count] = (char*)malloc(strlen(ents[i].w) + 1);
        strcpy(ans[count], ents[i].w);
        count++;
    }
    *returnSize = count;
    return ans;
}
