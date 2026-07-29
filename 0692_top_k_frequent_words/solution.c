// LeetCode 0692 - Top K Frequent Words
// https://leetcode.com/problems/top-k-frequent-words/

#define _POSIX_C_SOURCE 200809L
#include <stdlib.h>
#include <string.h>

typedef struct { char* word; int count; } Item;

static int cmpItem(const void* a, const void* b) {
    const Item* x = (const Item*)a;
    const Item* y = (const Item*)b;
    if (x->count != y->count) return y->count - x->count;
    return strcmp(x->word, y->word);
}

char** topKFrequent(char** words, int wordsSize, int k, int* returnSize) {
    Item* items = (Item*)malloc((size_t)wordsSize * sizeof(Item));
    int n = 0;
    for (int i = 0; i < wordsSize; i++) {
        int found = -1;
        for (int j = 0; j < n; j++) if (strcmp(items[j].word, words[i]) == 0) { found = j; break; }
        if (found >= 0) items[found].count++;
        else { items[n].word = words[i]; items[n].count = 1; n++; }
    }
    qsort(items, (size_t)n, sizeof(Item), cmpItem);
    char** result = (char**)malloc((size_t)k * sizeof(char*));
    for (int i = 0; i < k; i++) result[i] = strdup(items[i].word);
    free(items);
    *returnSize = k;
    return result;
}
