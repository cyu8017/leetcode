// LeetCode 0497 - Random Point in Non-overlapping Rectangles
// https://leetcode.com/problems/random-point-in-non-overlapping-rectangles/

#include <stdlib.h>

typedef struct {
    int** rects;
    int rectsSize;
    int* prefix;
    int total;
} Solution;

typedef double (*UniformFn)(double, double);

static UniformFn uniform = NULL;

static double defaultUniform(double low, double high) {
    (void)high;
    return low;
}

void set_uniform(UniformFn uniformFn) {
    uniform = uniformFn ? uniformFn : defaultUniform;
}

Solution* solutionCreate(int** rects, int rectsSize, int* rectsColSize) {
    (void)rectsColSize;
    Solution* obj = (Solution*)calloc(1, sizeof(Solution));
    obj->rects = rects;
    obj->rectsSize = rectsSize;
    obj->prefix = (int*)malloc((size_t)rectsSize * sizeof(int));
    for (int index = 0; index < rectsSize; index++) {
        const int* rect = rects[index];
        obj->total += (rect[2] - rect[0] + 1) * (rect[3] - rect[1] + 1);
        obj->prefix[index] = obj->total;
    }
    if (!uniform) {
        uniform = defaultUniform;
    }
    return obj;
}

int* solutionPick(Solution* obj, int* returnSize) {
    int index = (int)uniform(0, obj->total);
    if (index >= obj->total) {
        index = obj->total - 1;
    }

    int lo = 0;
    int hi = obj->rectsSize - 1;
    while (lo < hi) {
        const int mid = lo + (hi - lo) / 2;
        if (index < obj->prefix[mid]) {
            hi = mid;
        } else {
            lo = mid + 1;
        }
    }
    if (lo > 0) {
        index -= obj->prefix[lo - 1];
    }

    const int* rect = obj->rects[lo];
    const int width = rect[2] - rect[0] + 1;
    int* result = (int*)malloc(2 * sizeof(int));
    result[0] = rect[0] + index % width;
    result[1] = rect[1] + index / width;
    *returnSize = 2;
    return result;
}

void solutionFree(Solution* obj) {
    if (!obj) {
        return;
    }
    free(obj->prefix);
    free(obj);
}
