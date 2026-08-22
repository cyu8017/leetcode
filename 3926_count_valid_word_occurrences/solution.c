// LeetCode 3926 - Count Valid Word Occurrences
// https://leetcode.com/problems/count-valid-word-occurrences/

#include <stdlib.h>
#include <string.h>

enum { HS3926 = 4099 };
typedef struct { char* key; int val; int used; } Ent3926;
static Ent3926 ht3926[HS3926];

static unsigned hash3926(const char* s, int len) {
    unsigned h = 5381;
    for (int i = 0; i < len; i++) h = h * 33 + (unsigned char)s[i];
    return h % HS3926;
}
static void htAdd3926(const char* s, int len) {
    unsigned h = hash3926(s, len);
    for (;;) {
        if (!ht3926[h].used) {
            ht3926[h].used = 1;
            ht3926[h].key = malloc((size_t)len + 1);
            memcpy(ht3926[h].key, s, (size_t)len);
            ht3926[h].key[len] = 0;
            ht3926[h].val = 1;
            return;
        }
        if ((int)strlen(ht3926[h].key) == len && memcmp(ht3926[h].key, s, (size_t)len) == 0) {
            ht3926[h].val++;
            return;
        }
        h = (h + 1) % HS3926;
    }
}
static int htGet3926(const char* s) {
    int len = (int)strlen(s);
    unsigned h = hash3926(s, len);
    for (;;) {
        if (!ht3926[h].used) return 0;
        if ((int)strlen(ht3926[h].key) == len && memcmp(ht3926[h].key, s, (size_t)len) == 0)
            return ht3926[h].val;
        h = (h + 1) % HS3926;
    }
}

int* countWordOccurrences(char** chunks, int chunksSize, char** queries, int queriesSize, int* returnSize) {
    memset(ht3926, 0, sizeof(ht3926));
    int total = 1;
    for (int i = 0; i < chunksSize; i++) total += (int)strlen(chunks[i]);
    char* s = malloc((size_t)total);
    s[0] = 0;
    for (int i = 0; i < chunksSize; i++) strcat(s, chunks[i]);
    int n = (int)strlen(s);
    int i = 0;
    while (i < n) {
        if (s[i] == ' ' || s[i] == '-') { i++; continue; }
        int j = i;
        while (j < n && s[j] != ' ' && !(s[j] == '-' && (j + 1 >= n || s[j + 1] == ' ' || s[j + 1] == '-')))
            j++;
        htAdd3926(s + i, j - i);
        i = j;
    }
    int* ans = malloc((size_t)queriesSize * sizeof(int));
    for (int k = 0; k < queriesSize; k++) ans[k] = htGet3926(queries[k]);
    for (int k = 0; k < HS3926; k++) if (ht3926[k].used) free(ht3926[k].key);
    free(s);
    *returnSize = queriesSize;
    return ans;
}
