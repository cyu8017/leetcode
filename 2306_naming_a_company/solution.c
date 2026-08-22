// LeetCode 2306 - Naming a Company
// https://leetcode.com/problems/naming-a-company/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#define SUF_HASH 10007

typedef struct SufNode {
    char* s;
    struct SufNode* next;
} SufNode;

static unsigned hash_str(const char* s) {
    unsigned h = 2166136261u;
    while (*s) { h ^= (unsigned char)(*s++); h *= 16777619u; }
    return h % SUF_HASH;
}

static bool has_suf(SufNode** tab, const char* s) {
    unsigned h = hash_str(s);
    for (SufNode* p = tab[h]; p; p = p->next) {
        if (strcmp(p->s, s) == 0) return true;
    }
    return false;
}

static void add_suf(SufNode** tab, char* s) {
    if (has_suf(tab, s)) return;
    unsigned h = hash_str(s);
    SufNode* n = (SufNode*)malloc(sizeof(SufNode));
    n->s = s;
    n->next = tab[h];
    tab[h] = n;
}

static int count_group(SufNode** tab) {
    int c = 0;
    for (int i = 0; i < SUF_HASH; i++)
        for (SufNode* p = tab[i]; p; p = p->next) c++;
    return c;
}

static void free_group(SufNode** tab) {
    for (int i = 0; i < SUF_HASH; i++) {
        SufNode* p = tab[i];
        while (p) { SufNode* n = p->next; free(p); p = n; }
        tab[i] = NULL;
    }
}

long long distinctNames(char** ideas, int ideasSize) {
    SufNode* groups[26][SUF_HASH];
    memset(groups, 0, sizeof(groups));
    char** suffixes = (char**)malloc((size_t)ideasSize * sizeof(char*));
    for (int i = 0; i < ideasSize; i++) {
        suffixes[i] = ideas[i] + 1;
        add_suf(groups[ideas[i][0] - 'a'], suffixes[i]);
    }
    long long ans = 0;
    int sizes[26];
    for (int i = 0; i < 26; i++) sizes[i] = count_group(groups[i]);
    for (int i = 0; i < 26; i++) {
        for (int j = i + 1; j < 26; j++) {
            int overlap = 0;
            for (int h = 0; h < SUF_HASH; h++) {
                for (SufNode* p = groups[i][h]; p; p = p->next) {
                    if (has_suf(groups[j], p->s)) overlap++;
                }
            }
            ans += (long long)(sizes[i] - overlap) * (sizes[j] - overlap) * 2;
        }
    }
    for (int i = 0; i < 26; i++) free_group(groups[i]);
    free(suffixes);
    return ans;
}
