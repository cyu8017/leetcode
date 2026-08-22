// LeetCode 0447 - Number of Boomerangs
// https://leetcode.com/problems/number-of-boomerangs/

#include <stdlib.h>
#include <string.h>

typedef struct {
    int key;
    int value;
    int used;
} DistEntry;

static unsigned int hashInt(int key, int capacity) {
    unsigned int x = (unsigned int)key;
    x ^= x >> 16;
    x *= 0x7feb352du;
    x ^= x >> 15;
    return x % (unsigned int)capacity;
}

static void distAdd(DistEntry* table, int capacity, int key) {
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

int numberOfBoomerangs(int** points, int pointsSize, int* pointsColSize) {
    (void)pointsColSize;
    int total = 0;
    int capacity = pointsSize * 2 + 7;
    DistEntry* table = (DistEntry*)malloc((size_t)capacity * sizeof(DistEntry));

    for (int i = 0; i < pointsSize; i++) {
        memset(table, 0, (size_t)capacity * sizeof(DistEntry));
        for (int j = 0; j < pointsSize; j++) {
            int dx = points[i][0] - points[j][0];
            int dy = points[i][1] - points[j][1];
            distAdd(table, capacity, dx * dx + dy * dy);
        }
        for (int t = 0; t < capacity; t++) {
            if (table[t].used) {
                int count = table[t].value;
                total += count * (count - 1);
            }
        }
    }

    free(table);
    return total;
}
