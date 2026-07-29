// LeetCode 1257 - Smallest Common Region
// https://leetcode.com/problems/smallest-common-region/

#include <stdlib.h>
#include <string.h>

typedef struct {
    char key[64];
    char parent[64];
    int used;
} MapEntry;

static void map_put(MapEntry* map, int cap, const char* key, const char* parent) {
    unsigned h = 5381;
    for (const char* p = key; *p; p++) h = h * 33 + (unsigned char)*p;
    unsigned idx = h % (unsigned)cap;
    while (map[idx].used && strcmp(map[idx].key, key) != 0) idx = (idx + 1) % (unsigned)cap;
    if (!map[idx].used) {
        strncpy(map[idx].key, key, sizeof(map[idx].key) - 1);
        map[idx].used = 1;
    }
    strncpy(map[idx].parent, parent, sizeof(map[idx].parent) - 1);
}

static char* map_get(MapEntry* map, int cap, const char* key) {
    unsigned h = 5381;
    for (const char* p = key; *p; p++) h = h * 33 + (unsigned char)*p;
    unsigned idx = h % (unsigned)cap;
    while (map[idx].used) {
        if (strcmp(map[idx].key, key) == 0) return map[idx].parent;
        idx = (idx + 1) % (unsigned)cap;
    }
    return NULL;
}

char* findSmallestRegion(char*** regions, int regionsSize, int* regionsColSize, char* region1, char* region2) {
    (void)regionsColSize;
    int cap = regionsSize * 16 + 32;
    MapEntry* map = (MapEntry*)calloc((size_t)cap, sizeof(MapEntry));
    for (int i = 0; i < regionsSize; i++) {
        for (int j = 1; regions[i][j]; j++) map_put(map, cap, regions[i][j], regions[i][0]);
    }
    char* seen[256];
    int seenCount = 0;
    for (char* cur = region1; cur; cur = map_get(map, cap, cur)) seen[seenCount++] = cur;
    for (char* cur = region2; cur; cur = map_get(map, cap, cur)) {
        for (int i = 0; i < seenCount; i++) {
            if (strcmp(seen[i], cur) == 0) {
                free(map);
                return cur;
            }
        }
    }
    free(map);
    return region1;
}
