// LeetCode 0893 - Groups of Special-Equivalent Strings
// https://leetcode.com/problems/groups-of-special-equivalent-strings/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <stdio.h>

static int cmp_char(const void* a, const void* b) {
    return *(const char*)a - *(const char*)b;
}

static void key_of(const char* w, char* out) {
    char even[40] = {0}, odd[40] = {0};
    int e = 0, o = 0;
    for (int i = 0; w[i]; i++) {
        if (i % 2 == 0) even[e++] = w[i];
        else odd[o++] = w[i];
    }
    qsort(even, (size_t)e, 1, cmp_char);
    qsort(odd, (size_t)o, 1, cmp_char);
    sprintf(out, "%s|%s", even, odd);
}

int numSpecialEquivGroups(char** words, int wordsSize) {
    char keys[300][80];
    int nk = 0;
    for (int i = 0; i < wordsSize; i++) {
        char k[80];
        key_of(words[i], k);
        bool found = false;
        for (int j = 0; j < nk; j++) if (strcmp(keys[j], k) == 0) { found = true; break; }
        if (!found) strcpy(keys[nk++], k);
    }
    return nk;
}
