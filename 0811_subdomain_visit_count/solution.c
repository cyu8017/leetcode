// LeetCode 0811 - Subdomain Visit Count
// https://leetcode.com/problems/subdomain-visit-count/

#include <stdlib.h>
#include <string.h>
#include <stdio.h>

typedef struct { char* domain; int count; } Entry;

char** subdomainVisits(char** cpdomains, int cpdomainsSize, int* returnSize) {
    Entry* entries = (Entry*)calloc(300, sizeof(Entry));
    int nent = 0;
    for (int i = 0; i < cpdomainsSize; i++) {
        int count = 0;
        const char* p = cpdomains[i];
        while (*p >= '0' && *p <= '9') { count = count * 10 + (*p - '0'); p++; }
        if (*p == ' ') p++;
        char domain[120];
        strcpy(domain, p);
        char* parts[10];
        int np = 0;
        char tmp[120];
        strcpy(tmp, domain);
        for (char* tok = strtok(tmp, "."); tok; tok = strtok(NULL, "."))
            parts[np++] = tok;
        for (int s = 0; s < np; s++) {
            char buf[120] = {0};
            for (int j = s; j < np; j++) {
                if (j > s) strcat(buf, ".");
                strcat(buf, parts[j]);
            }
            int found = -1;
            for (int e = 0; e < nent; e++)
                if (strcmp(entries[e].domain, buf) == 0) { found = e; break; }
            if (found >= 0) entries[found].count += count;
            else {
                entries[nent].domain = (char*)malloc(strlen(buf) + 1);
                strcpy(entries[nent].domain, buf);
                entries[nent].count = count;
                nent++;
            }
        }
    }
    char** ans = (char**)malloc((size_t)nent * sizeof(char*));
    for (int i = 0; i < nent; i++) {
        ans[i] = (char*)malloc(140);
        sprintf(ans[i], "%d %s", entries[i].count, entries[i].domain);
        free(entries[i].domain);
    }
    free(entries);
    *returnSize = nent;
    return ans;
}
