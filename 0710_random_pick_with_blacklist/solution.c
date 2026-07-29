// LeetCode 0710 - Random Pick with Blacklist
// https://leetcode.com/problems/random-pick-with-blacklist/

#include <stdlib.h>
#include <stdbool.h>

typedef struct {
    int* keys;
    int* vals;
    int mapSize;
    int size;
} Solution;

static int mapGet(Solution* obj, int key, bool* found) {
    for (int i = 0; i < obj->mapSize; i++) {
        if (obj->keys[i] == key) {
            *found = true;
            return obj->vals[i];
        }
    }
    *found = false;
    return 0;
}

Solution* solutionCreate(int n, int* blacklist, int blacklistSize) {
    Solution* obj = (Solution*)malloc(sizeof(Solution));
    obj->size = n - blacklistSize;
    obj->keys = NULL;
    obj->vals = NULL;
    obj->mapSize = 0;

    bool* black = (bool*)calloc((size_t)n, sizeof(bool));
    for (int i = 0; i < blacklistSize; i++) {
        if (blacklist[i] >= 0 && blacklist[i] < n) {
            black[blacklist[i]] = true;
        }
    }

    int* whites = (int*)malloc((size_t)blacklistSize * sizeof(int));
    int w = 0;
    for (int x = obj->size; x < n; x++) {
        if (!black[x]) {
            whites[w++] = x;
        }
    }

    int wi = 0;
    int cap = 0;
    for (int i = 0; i < blacklistSize; i++) {
        int b = blacklist[i];
        if (b < obj->size) {
            if (obj->mapSize == cap) {
                cap = cap ? cap * 2 : 8;
                obj->keys = (int*)realloc(obj->keys, (size_t)cap * sizeof(int));
                obj->vals = (int*)realloc(obj->vals, (size_t)cap * sizeof(int));
            }
            obj->keys[obj->mapSize] = b;
            obj->vals[obj->mapSize] = whites[wi++];
            obj->mapSize++;
        }
    }

    free(whites);
    free(black);
    return obj;
}

int solutionPick(Solution* obj) {
    int index = rand() % obj->size;
    bool found = false;
    int mapped = mapGet(obj, index, &found);
    return found ? mapped : index;
}

void solutionFree(Solution* obj) {
    free(obj->keys);
    free(obj->vals);
    free(obj);
}
