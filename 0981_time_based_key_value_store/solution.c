// LeetCode 0981 - Time Based Key-Value Store
// https://leetcode.com/problems/time-based-key-value-store/

#include <stdlib.h>
#include <string.h>

typedef struct { int ts; char* val; } Entry;
typedef struct { char* key; Entry* entries; int n, cap; } Bucket;
typedef struct { Bucket* buckets; int bn, bcap; } TimeMap;

TimeMap* timeMapCreate(void) {
    TimeMap* obj = (TimeMap*)calloc(1, sizeof(TimeMap));
    obj->bcap = 64;
    obj->buckets = (Bucket*)calloc((size_t)obj->bcap, sizeof(Bucket));
    return obj;
}

static Bucket* findBucket(TimeMap* obj, char* key, int create) {
    for (int i = 0; i < obj->bn; i++) if (strcmp(obj->buckets[i].key, key) == 0) return &obj->buckets[i];
    if (!create) return NULL;
    if (obj->bn == obj->bcap) {
        obj->bcap *= 2;
        obj->buckets = (Bucket*)realloc(obj->buckets, (size_t)obj->bcap * sizeof(Bucket));
        memset(obj->buckets + obj->bn, 0, (size_t)(obj->bcap - obj->bn) * sizeof(Bucket));
    }
    Bucket* b = &obj->buckets[obj->bn++];
    b->key = key;
    b->cap = 8; b->n = 0;
    b->entries = (Entry*)malloc((size_t)b->cap * sizeof(Entry));
    return b;
}

void timeMapSet(TimeMap* obj, char* key, char* value, int timestamp) {
    Bucket* b = findBucket(obj, key, 1);
    if (b->n == b->cap) {
        b->cap *= 2;
        b->entries = (Entry*)realloc(b->entries, (size_t)b->cap * sizeof(Entry));
    }
    b->entries[b->n].ts = timestamp;
    b->entries[b->n].val = value;
    b->n++;
}

char* timeMapGet(TimeMap* obj, char* key, int timestamp) {
    Bucket* b = findBucket(obj, key, 0);
    if (!b || b->n == 0) return "";
    int lo = 0, hi = b->n - 1, ans = -1;
    while (lo <= hi) {
        int mid = lo + (hi - lo) / 2;
        if (b->entries[mid].ts <= timestamp) { ans = mid; lo = mid + 1; }
        else hi = mid - 1;
    }
    return ans >= 0 ? b->entries[ans].val : "";
}

void timeMapFree(TimeMap* obj) {
    for (int i = 0; i < obj->bn; i++) free(obj->buckets[i].entries);
    free(obj->buckets);
    free(obj);
}
