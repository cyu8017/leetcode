// LeetCode 3137 - Minimum Number of Operations to Make Word K-Periodic
// https://leetcode.com/problems/minimum-number-of-operations-to-make-word-k-periodic/

#include <stdlib.h>
#include <string.h>

enum { H3137 = 10007 };
typedef struct { char* s; int val; int used; } E3137;

int minimumOperationsToMakeKPeriodic(char* word, int k) {
    int n = (int)strlen(word);
    E3137* ht = calloc(H3137, sizeof(E3137));
    int mx = 0;
    for (int i = 0; i < n; i += k) {
        char* s = malloc(k + 1);
        memcpy(s, word + i, k); s[k] = 0;
        unsigned h = 0;
        for (int j = 0; j < k; j++) h = h * 131u + (unsigned char)s[j];
        h %= H3137;
        while (ht[h].used && strcmp(ht[h].s, s) != 0) h = (h + 1) % H3137;
        if (!ht[h].used) { ht[h].used = 1; ht[h].s = s; ht[h].val = 0; }
        else free(s);
        ht[h].val++;
        if (ht[h].val > mx) mx = ht[h].val;
    }
    for (int i = 0; i < H3137; i++) if (ht[i].used) free(ht[i].s);
    free(ht);
    return n / k - mx;
}
