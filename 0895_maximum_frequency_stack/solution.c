// LeetCode 0895 - Maximum Frequency Stack
// https://leetcode.com/problems/maximum-frequency-stack/

#include <stdlib.h>
#include <limits.h>

typedef struct {
    int* freq;       // hashed open addressing for val -> freq; use parallel arrays
    int* keys;
    int* fvals;
    int cap;
    int** group;     // group[f] stack
    int* gsz;
    int* gcap;
    int maxGroup;
    int maxfreq;
} FreqStack;

static int find_slot(FreqStack* obj, int val, int create) {
    unsigned h = ((unsigned)val * 2654435761u) & (unsigned)(obj->cap - 1);
    while (obj->keys[h] != INT_MIN) {
        if (obj->keys[h] == val) return (int)h;
        h = (h + 1) & (unsigned)(obj->cap - 1);
    }
    if (!create) return -1;
    obj->keys[h] = val;
    obj->fvals[h] = 0;
    return (int)h;
}

FreqStack* freqStackCreate() {
    FreqStack* obj = (FreqStack*)calloc(1, sizeof(FreqStack));
    obj->cap = 1 << 14;
    obj->keys = (int*)malloc((size_t)obj->cap * sizeof(int));
    obj->fvals = (int*)calloc((size_t)obj->cap, sizeof(int));
    for (int i = 0; i < obj->cap; i++) obj->keys[i] = INT_MIN;
    obj->maxGroup = 64;
    obj->group = (int**)calloc((size_t)obj->maxGroup, sizeof(int*));
    obj->gsz = (int*)calloc((size_t)obj->maxGroup, sizeof(int));
    obj->gcap = (int*)calloc((size_t)obj->maxGroup, sizeof(int));
    obj->maxfreq = 0;
    return obj;
}

void freqStackPush(FreqStack* obj, int val) {
    int slot = find_slot(obj, val, 1);
    int f = ++obj->fvals[slot];
    if (f > obj->maxfreq) obj->maxfreq = f;
    if (f >= obj->maxGroup) {
        int old = obj->maxGroup;
        obj->maxGroup = f * 2;
        obj->group = (int**)realloc(obj->group, (size_t)obj->maxGroup * sizeof(int*));
        obj->gsz = (int*)realloc(obj->gsz, (size_t)obj->maxGroup * sizeof(int));
        obj->gcap = (int*)realloc(obj->gcap, (size_t)obj->maxGroup * sizeof(int));
        for (int i = old; i < obj->maxGroup; i++) {
            obj->group[i] = NULL; obj->gsz[i] = 0; obj->gcap[i] = 0;
        }
    }
    if (obj->gsz[f] == obj->gcap[f]) {
        obj->gcap[f] = obj->gcap[f] ? obj->gcap[f] * 2 : 8;
        obj->group[f] = (int*)realloc(obj->group[f], (size_t)obj->gcap[f] * sizeof(int));
    }
    obj->group[f][obj->gsz[f]++] = val;
}

int freqStackPop(FreqStack* obj) {
    int f = obj->maxfreq;
    int val = obj->group[f][--obj->gsz[f]];
    int slot = find_slot(obj, val, 0);
    obj->fvals[slot]--;
    if (obj->gsz[f] == 0) obj->maxfreq--;
    return val;
}

void freqStackFree(FreqStack* obj) {
    free(obj->keys); free(obj->fvals);
    for (int i = 0; i < obj->maxGroup; i++) free(obj->group[i]);
    free(obj->group); free(obj->gsz); free(obj->gcap);
    free(obj);
}
