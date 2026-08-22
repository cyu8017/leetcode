// LeetCode 2631 - Group By
// https://leetcode.com/problems/group-by/

#include <stdlib.h>
#include <string.h>

// JavaScript problem; C stand-in groups ints by key function returning int bucket.
typedef int (*KeyFn)(int);

typedef struct {
    int* items;
    int size;
    int cap;
} Bucket;

typedef struct {
    Bucket* buckets;
    int* keys;
    int size;
    int cap;
} GroupResult;

GroupResult* groupBy(int* arr, int arrSize, KeyFn fn) {
    GroupResult* out = (GroupResult*)calloc(1, sizeof(GroupResult));
    out->cap = 16;
    out->buckets = (Bucket*)calloc((size_t)out->cap, sizeof(Bucket));
    out->keys = (int*)malloc((size_t)out->cap * sizeof(int));
    for (int i = 0; i < arrSize; i++) {
        int k = fn(arr[i]);
        int idx = -1;
        for (int j = 0; j < out->size; j++) if (out->keys[j] == k) { idx = j; break; }
        if (idx < 0) {
            if (out->size == out->cap) {
                out->cap *= 2;
                out->buckets = (Bucket*)realloc(out->buckets, (size_t)out->cap * sizeof(Bucket));
                out->keys = (int*)realloc(out->keys, (size_t)out->cap * sizeof(int));
                for (int j = out->size; j < out->cap; j++) {
                    out->buckets[j].items = NULL;
                    out->buckets[j].size = 0;
                    out->buckets[j].cap = 0;
                }
            }
            idx = out->size;
            out->keys[idx] = k;
            out->size++;
        }
        Bucket* b = &out->buckets[idx];
        if (b->size == b->cap) {
            b->cap = b->cap ? b->cap * 2 : 4;
            b->items = (int*)realloc(b->items, (size_t)b->cap * sizeof(int));
        }
        b->items[b->size++] = arr[i];
    }
    return out;
}

void groupResultFree(GroupResult* out) {
    if (!out) return;
    for (int i = 0; i < out->size; i++) free(out->buckets[i].items);
    free(out->buckets); free(out->keys); free(out);
}
