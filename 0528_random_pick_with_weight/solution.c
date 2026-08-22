// LeetCode 0528 - Random Pick with Weight
// https://leetcode.com/problems/random-pick-with-weight/

#include <stdlib.h>

typedef struct {
    int* prefix;
    int prefixSize;
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

static int bisectRight(const int* values, int valuesSize, int target) {
    int low = 0;
    int high = valuesSize - 1;
    while (low < high) {
        const int mid = low + (high - low) / 2;
        if (values[mid] <= target) {
            low = mid + 1;
        } else {
            high = mid;
        }
    }
    return low;
}

Solution* solutionCreate(int* w, int wSize) {
    Solution* obj = (Solution*)calloc(1, sizeof(Solution));
    obj->prefix = (int*)malloc((size_t)wSize * sizeof(int));
    obj->prefixSize = wSize;
    int runningTotal = 0;
    for (int index = 0; index < wSize; index++) {
        runningTotal += w[index];
        obj->prefix[index] = runningTotal;
    }
    obj->total = runningTotal;
    if (!uniform) {
        uniform = defaultUniform;
    }
    return obj;
}

int solutionPickIndex(Solution* obj) {
    int target = (int)uniform(0, obj->total);
    if (target >= obj->total) {
        target = obj->total - 1;
    }
    return bisectRight(obj->prefix, obj->prefixSize, target);
}

void solutionFree(Solution* obj) {
    if (!obj) {
        return;
    }
    free(obj->prefix);
    free(obj);
}
