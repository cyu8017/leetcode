// LeetCode 3093 - Longest Common Suffix Queries
// https://leetcode.com/problems/longest-common-suffix-queries/

#include <stdlib.h>
#include <string.h>

#define INF3093 (1 << 30)

typedef struct Trie {
    struct Trie* children[26];
    int length;
    int idx;
} Trie;

static Trie* newTrie(void) {
    Trie* t = (Trie*)calloc(1, sizeof(Trie));
    t->length = INF3093; t->idx = INF3093;
    return t;
}
static void trieInsert(Trie* t, const char* w, int i) {
    Trie* node = t;
    int len = (int)strlen(w);
    if (node->length > len) { node->length = len; node->idx = i; }
    for (int k = len - 1; k >= 0; k--) {
        int id = w[k] - 'a';
        if (!node->children[id]) node->children[id] = newTrie();
        node = node->children[id];
        if (node->length > len) { node->length = len; node->idx = i; }
    }
}
static int trieQuery(Trie* t, const char* w) {
    Trie* node = t;
    int len = (int)strlen(w);
    for (int k = len - 1; k >= 0; k--) {
        int id = w[k] - 'a';
        if (!node->children[id]) break;
        node = node->children[id];
    }
    return node->idx;
}
static void freeTrie(Trie* t) {
    if (!t) return;
    for (int i = 0; i < 26; i++) freeTrie(t->children[i]);
    free(t);
}

int* stringIndices(char** wordsContainer, int wordsContainerSize, char** wordsQuery, int wordsQuerySize, int* returnSize) {
    Trie* trie = newTrie();
    for (int i = 0; i < wordsContainerSize; i++) trieInsert(trie, wordsContainer[i], i);
    int* ans = (int*)malloc((size_t)wordsQuerySize * sizeof(int));
    for (int i = 0; i < wordsQuerySize; i++) ans[i] = trieQuery(trie, wordsQuery[i]);
    freeTrie(trie);
    *returnSize = wordsQuerySize;
    return ans;
}
