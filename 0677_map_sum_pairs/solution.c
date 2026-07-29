// LeetCode 0677 - Map Sum Pairs
// https://leetcode.com/problems/map-sum-pairs/

#define _POSIX_C_SOURCE 200809L
#include <stdlib.h>
#include <string.h>

typedef struct {
    char** keys;
    int* values;
    int size;
    int capacity;
} MapSum;

MapSum* mapSumCreate() {
    MapSum* obj = (MapSum*)malloc(sizeof(MapSum));
    obj->capacity = 16;
    obj->keys = (char**)malloc((size_t)obj->capacity * sizeof(char*));
    obj->values = (int*)malloc((size_t)obj->capacity * sizeof(int));
    obj->size = 0;
    return obj;
}

void mapSumInsert(MapSum* obj, char* key, int val) {
    for (int i = 0; i < obj->size; i++) {
        if (strcmp(obj->keys[i], key) == 0) { obj->values[i] = val; return; }
    }
    if (obj->size == obj->capacity) {
        obj->capacity *= 2;
        obj->keys = (char**)realloc(obj->keys, (size_t)obj->capacity * sizeof(char*));
        obj->values = (int*)realloc(obj->values, (size_t)obj->capacity * sizeof(int));
    }
    obj->keys[obj->size] = strdup(key);
    obj->values[obj->size] = val;
    obj->size++;
}

int mapSumSum(MapSum* obj, char* prefix) {
    int plen = (int)strlen(prefix);
    int sum = 0;
    for (int i = 0; i < obj->size; i++) {
        if (strncmp(obj->keys[i], prefix, (size_t)plen) == 0) sum += obj->values[i];
    }
    return sum;
}

void mapSumFree(MapSum* obj) {
    for (int i = 0; i < obj->size; i++) free(obj->keys[i]);
    free(obj->keys); free(obj->values); free(obj);
}
