// LeetCode 0554 - Brick Wall
// https://leetcode.com/problems/brick-wall/

#include <stdlib.h>

typedef struct {
    int key;
    int value;
    int used;
} EdgeEntry;

static unsigned int hashInt(int key, int capacity) {
    unsigned int x = (unsigned int)key;
    x ^= x >> 16;
    x *= 0x7feb352du;
    x ^= x >> 15;
    return x % (unsigned int)capacity;
}

static void edgeAdd(EdgeEntry* table, int capacity, int key) {
    unsigned int idx = hashInt(key, capacity);
    while (table[idx].used && table[idx].key != key) {
        idx = (idx + 1) % (unsigned int)capacity;
    }
    if (!table[idx].used) {
        table[idx].used = 1;
        table[idx].key = key;
        table[idx].value = 0;
    }
    table[idx].value++;
}

int leastBricks(int** wall, int wallSize, int* wallColSize) {
    int capacity = wallSize * 64 + 7;
    EdgeEntry* table = (EdgeEntry*)calloc((size_t)capacity, sizeof(EdgeEntry));
    for (int i = 0; i < wallSize; i++) {
        int width = 0;
        for (int j = 0; j < wallColSize[i] - 1; j++) {
            width += wall[i][j];
            edgeAdd(table, capacity, width);
        }
    }

    int best = 0;
    for (int i = 0; i < capacity; i++) {
        if (table[i].used && table[i].value > best) {
            best = table[i].value;
        }
    }
    free(table);
    return wallSize - best;
}
