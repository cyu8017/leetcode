// LeetCode 0391 - Perfect Rectangle
// https://leetcode.com/problems/perfect-rectangle/

#include <limits.h>
#include <stdbool.h>
#include <stdlib.h>

typedef struct {
    int x;
    int y;
} Point;

static int findPoint(Point* points, int count, int x, int y) {
    for (int index = 0; index < count; index++) {
        if (points[index].x == x && points[index].y == y) {
            return index;
        }
    }
    return -1;
}

static void togglePoint(Point** points, int* count, int* capacity, int x, int y) {
    int found = findPoint(*points, *count, x, y);
    if (found >= 0) {
        (*points)[found] = (*points)[*count - 1];
        *count -= 1;
        return;
    }

    if (*count == *capacity) {
        *capacity = *capacity == 0 ? 4 : *capacity * 2;
        *points = (Point*)realloc(*points, (size_t)(*capacity) * sizeof(Point));
    }
    (*points)[*count].x = x;
    (*points)[*count].y = y;
    *count += 1;
}

static bool hasPoint(Point* points, int count, int x, int y) {
    return findPoint(points, count, x, y) >= 0;
}

bool isRectangleCover(int** rectangles, int rectanglesSize, int* rectanglesColSize) {
    (void)rectanglesColSize;

    Point* points = NULL;
    int pointCount = 0;
    int pointCapacity = 0;
    long long area = 0;
    int minX = INT_MAX;
    int minY = INT_MAX;
    int maxX = INT_MIN;
    int maxY = INT_MIN;

    for (int index = 0; index < rectanglesSize; index++) {
        int x1 = rectangles[index][0];
        int y1 = rectangles[index][1];
        int x2 = rectangles[index][2];
        int y2 = rectangles[index][3];
        area += (long long)(x2 - x1) * (y2 - y1);
        minX = x1 < minX ? x1 : minX;
        minY = y1 < minY ? y1 : minY;
        maxX = x2 > maxX ? x2 : maxX;
        maxY = y2 > maxY ? y2 : maxY;

        togglePoint(&points, &pointCount, &pointCapacity, x1, y1);
        togglePoint(&points, &pointCount, &pointCapacity, x1, y2);
        togglePoint(&points, &pointCount, &pointCapacity, x2, y1);
        togglePoint(&points, &pointCount, &pointCapacity, x2, y2);
    }

    bool valid = pointCount == 4 && hasPoint(points, pointCount, minX, minY) &&
                 hasPoint(points, pointCount, minX, maxY) &&
                 hasPoint(points, pointCount, maxX, minY) &&
                 hasPoint(points, pointCount, maxX, maxY) &&
                 area == (long long)(maxX - minX) * (maxY - minY);

    free(points);
    return valid;
}
