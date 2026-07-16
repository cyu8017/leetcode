// LeetCode 0356 - Line Reflection
// https://leetcode.com/problems/line-reflection/

#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    long long key;
    int used;
} PointEntry;

static long long pointKey(int x, int y) {
    return ((long long)x << 32) | (unsigned int)y;
}

static int findPoint(PointEntry* entries, int count, long long key) {
    for (int index = 0; index < count; index++) {
        if (entries[index].key == key) {
            return index;
        }
    }
    return -1;
}

bool isReflected(int** points, int pointsSize, int* pointsColSize) {
    (void)pointsColSize;
    if (pointsSize == 0) {
        return true;
    }

    PointEntry* entries = (PointEntry*)malloc((size_t)pointsSize * sizeof(PointEntry));
    int minX = points[0][0];
    int maxX = points[0][0];

    for (int index = 0; index < pointsSize; index++) {
        int x = points[index][0];
        int y = points[index][1];
        if (x < minX) {
            minX = x;
        }
        if (x > maxX) {
            maxX = x;
        }
        entries[index].key = pointKey(x, y);
        entries[index].used = 0;
    }

    int target = minX + maxX;
    for (int index = 0; index < pointsSize; index++) {
        int x = points[index][0];
        int y = points[index][1];
        long long mirrorKey = pointKey(target - x, y);
        if (findPoint(entries, pointsSize, mirrorKey) < 0) {
            free(entries);
            return false;
        }
    }

    free(entries);
    return true;
}
