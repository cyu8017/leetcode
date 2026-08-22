// LeetCode 0519 - Random Flip Matrix
// https://leetcode.com/problems/random-flip-matrix/

#include <stdlib.h>

typedef struct {
    int cols;
    int total;
    int* available;
    int availableSize;
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

Solution* solutionCreate(int m, int n) {
    Solution* obj = (Solution*)calloc(1, sizeof(Solution));
    obj->cols = n;
    obj->total = m * n;
    obj->available = (int*)malloc((size_t)obj->total * sizeof(int));
    obj->availableSize = obj->total;
    for (int index = 0; index < obj->total; index++) {
        obj->available[index] = index;
    }
    if (!uniform) {
        uniform = defaultUniform;
    }
    return obj;
}

int* solutionFlip(Solution* obj, int* returnSize) {
    int index = (int)uniform(0, obj->availableSize - 1);
    if (index >= obj->availableSize) {
        index = obj->availableSize - 1;
    }
    const int value = obj->available[index];
    obj->available[index] = obj->available[obj->availableSize - 1];
    obj->availableSize--;

    int* result = (int*)malloc(2 * sizeof(int));
    result[0] = value / obj->cols;
    result[1] = value % obj->cols;
    *returnSize = 2;
    return result;
}

void solutionReset(Solution* obj) {
    obj->availableSize = obj->total;
    for (int index = 0; index < obj->total; index++) {
        obj->available[index] = index;
    }
}

void solutionFree(Solution* obj) {
    if (!obj) {
        return;
    }
    free(obj->available);
    free(obj);
}
