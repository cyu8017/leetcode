// LeetCode 0761 - Special Binary String
#include <stdlib.h>
#include <string.h>

static int cmpRev(const void* a, const void* b) {
    return strcmp(*(char* const*)b, *(char* const*)a);
}

char* makeLargestSpecial(char* s) {
    int n = (int)strlen(s);
    if (n == 0) {
        char* e = (char*)malloc(1); e[0]='\0'; return e;
    }
    char** parts = (char**)malloc((size_t)n * sizeof(char*));
    int pcount = 0, balance = 0, start = 0;
    for (int i = 0; i < n; i++) {
        balance += s[i] == '1' ? 1 : -1;
        if (balance == 0) {
            char* mid = (char*)malloc((size_t)(i - start));
            memcpy(mid, s + start + 1, (size_t)(i - start - 1));
            mid[i - start - 1] = '\0';
            char* inner = makeLargestSpecial(mid);
            free(mid);
            char* part = (char*)malloc(strlen(inner) + 3);
            part[0] = '1';
            strcpy(part + 1, inner);
            strcat(part, "0");
            free(inner);
            parts[pcount++] = part;
            start = i + 1;
        }
    }
    qsort(parts, (size_t)pcount, sizeof(char*), cmpRev);
    int total = 1;
    for (int i = 0; i < pcount; i++) total += (int)strlen(parts[i]);
    char* out = (char*)malloc((size_t)total);
    out[0] = '\0';
    for (int i = 0; i < pcount; i++) { strcat(out, parts[i]); free(parts[i]); }
    free(parts);
    return out;
}
