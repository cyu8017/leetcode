// LeetCode 0587 - Erect the Fence
// https://leetcode.com/problems/erect-the-fence/

#include <stdlib.h>

typedef struct {
    int x;
    int y;
} Point;

static int cmpPoint(const void* a, const void* b) {
    const Point* left = (const Point*)a;
    const Point* right = (const Point*)b;
    if (left->x != right->x) {
        return left->x - right->x;
    }
    return left->y - right->y;
}

static long long cross(Point o, Point a, Point b) {
    return (long long)(a.x - o.x) * (b.y - o.y) - (long long)(a.y - o.y) * (b.x - o.x);
}

static int buildHull(Point* ordered, int size, Point* hull) {
    int top = 0;
    for (int i = 0; i < size; i++) {
        while (top >= 2 && cross(hull[top - 2], hull[top - 1], ordered[i]) < 0) {
            top--;
        }
        hull[top++] = ordered[i];
    }
    return top;
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** outerTrees(int** trees, int treesSize, int* treesColSize, int* returnSize, int** returnColumnSizes) {
    (void)treesColSize;
    Point* points = (Point*)malloc((size_t)treesSize * sizeof(Point));
    for (int i = 0; i < treesSize; i++) {
        points[i].x = trees[i][0];
        points[i].y = trees[i][1];
    }
    qsort(points, (size_t)treesSize, sizeof(Point), cmpPoint);

    if (treesSize <= 1) {
        *returnSize = treesSize;
        *returnColumnSizes = (int*)malloc((size_t)treesSize * sizeof(int));
        int** result = (int**)malloc((size_t)treesSize * sizeof(int*));
        for (int i = 0; i < treesSize; i++) {
            (*returnColumnSizes)[i] = 2;
            result[i] = (int*)malloc(2 * sizeof(int));
            result[i][0] = points[i].x;
            result[i][1] = points[i].y;
        }
        free(points);
        return result;
    }

    Point* lower = (Point*)malloc((size_t)treesSize * sizeof(Point));
    Point* upper = (Point*)malloc((size_t)treesSize * sizeof(Point));
    int lowerSize = buildHull(points, treesSize, lower);

    Point* reversed = (Point*)malloc((size_t)treesSize * sizeof(Point));
    for (int i = 0; i < treesSize; i++) {
        reversed[i] = points[treesSize - 1 - i];
    }
    int upperSize = buildHull(reversed, treesSize, upper);

    Point* hull = (Point*)malloc((size_t)(lowerSize + upperSize) * sizeof(Point));
    int hullSize = 0;
    for (int i = 0; i < lowerSize - 1; i++) {
        hull[hullSize++] = lower[i];
    }
    for (int i = 0; i < upperSize - 1; i++) {
        int duplicate = 0;
        for (int j = 0; j < hullSize; j++) {
            if (hull[j].x == upper[i].x && hull[j].y == upper[i].y) {
                duplicate = 1;
                break;
            }
        }
        if (!duplicate) {
            hull[hullSize++] = upper[i];
        }
    }

    *returnSize = hullSize;
    *returnColumnSizes = (int*)malloc((size_t)hullSize * sizeof(int));
    int** result = (int**)malloc((size_t)hullSize * sizeof(int*));
    for (int i = 0; i < hullSize; i++) {
        (*returnColumnSizes)[i] = 2;
        result[i] = (int*)malloc(2 * sizeof(int));
        result[i][0] = hull[i].x;
        result[i][1] = hull[i].y;
    }

    free(points);
    free(lower);
    free(upper);
    free(reversed);
    free(hull);
    return result;
}
