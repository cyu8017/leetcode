// LeetCode 1487 - Making File Names Unique
// https://leetcode.com/problems/making-file-names-unique/

#include <stdlib.h>
#include <string.h>
#include <stdio.h>

typedef struct { char* name; int nextk; } Entry;

static int find_entry(Entry* used, int un, char* name) {
    for (int i = 0; i < un; i++) if (strcmp(used[i].name, name) == 0) return i;
    return -1;
}

char** getFolderNames(char** names, int namesSize, int* returnSize) {
    Entry* used = (Entry*)malloc(namesSize * 4 * sizeof(Entry));
    int un = 0;
    char** ans = (char**)malloc(namesSize * sizeof(char*));
    for (int i = 0; i < namesSize; i++) {
        char* name = names[i];
        char* candidate;
        int idx = find_entry(used, un, name);
        if (idx < 0) {
            candidate = (char*)malloc(strlen(name) + 1);
            strcpy(candidate, name);
        } else {
            int k = used[idx].nextk;
            char buf[300];
            while (1) {
                sprintf(buf, "%s(%d)", name, k);
                if (find_entry(used, un, buf) < 0) break;
                k++;
            }
            used[idx].nextk = k + 1;
            candidate = (char*)malloc(strlen(buf) + 1);
            strcpy(candidate, buf);
        }
        used[un].name = (char*)malloc(strlen(candidate) + 1);
        strcpy(used[un].name, candidate);
        used[un].nextk = 1;
        un++;
        ans[i] = candidate;
    }
    for (int i = 0; i < un; i++) free(used[i].name);
    free(used);
    *returnSize = namesSize;
    return ans;
}
