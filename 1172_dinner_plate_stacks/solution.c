// LeetCode 1172 - Dinner Plate Stacks
// https://leetcode.com/problems/dinner-plate-stacks/

#include <stdlib.h>

typedef struct {
    int capacity;
    int** stacks;
    int* stackSizes;
    int stacksCount;
    int stacksCap;
    int* available;
    int availSize;
    int availCap;
} DinnerPlates;

static void heapPush(int* h, int* n, int* cap, int v) {
    if (*n >= *cap) {
        *cap = *cap ? *cap * 2 : 8;
        // realloc handled by caller via pointer - use simple grow outside
    }
    int i = (*n)++;
    h[i] = v;
    while (i > 0) {
        int p = (i - 1) / 2;
        if (h[p] <= h[i]) break;
        int t = h[p]; h[p] = h[i]; h[i] = t;
        i = p;
    }
}

static int heapPop(int* h, int* n) {
    int top = h[0];
    h[0] = h[--(*n)];
    int i = 0;
    while (1) {
        int l = 2 * i + 1, r = 2 * i + 2, best = i;
        if (l < *n && h[l] < h[best]) best = l;
        if (r < *n && h[r] < h[best]) best = r;
        if (best == i) break;
        int t = h[best]; h[best] = h[i]; h[i] = t;
        i = best;
    }
    return top;
}

DinnerPlates* dinnerPlatesCreate(int capacity) {
    DinnerPlates* obj = (DinnerPlates*)calloc(1, sizeof(DinnerPlates));
    obj->capacity = capacity;
    obj->stacksCap = 8;
    obj->stacks = (int**)calloc((size_t)obj->stacksCap, sizeof(int*));
    obj->stackSizes = (int*)calloc((size_t)obj->stacksCap, sizeof(int));
    obj->availCap = 8;
    obj->available = (int*)malloc((size_t)obj->availCap * sizeof(int));
    return obj;
}

void dinnerPlatesPush(DinnerPlates* obj, int val) {
    while (obj->availSize && (obj->available[0] >= obj->stacksCount ||
           obj->stackSizes[obj->available[0]] == obj->capacity)) {
        heapPop(obj->available, &obj->availSize);
    }
    if (!obj->availSize) {
        if (obj->stacksCount >= obj->stacksCap) {
            obj->stacksCap *= 2;
            obj->stacks = (int**)realloc(obj->stacks, (size_t)obj->stacksCap * sizeof(int*));
            obj->stackSizes = (int*)realloc(obj->stackSizes, (size_t)obj->stacksCap * sizeof(int));
        }
        obj->stacks[obj->stacksCount] = (int*)malloc((size_t)obj->capacity * sizeof(int));
        obj->stackSizes[obj->stacksCount] = 0;
        if (obj->availSize >= obj->availCap) {
            obj->availCap *= 2;
            obj->available = (int*)realloc(obj->available, (size_t)obj->availCap * sizeof(int));
        }
        heapPush(obj->available, &obj->availSize, &obj->availCap, obj->stacksCount);
        obj->stacksCount++;
    }
    int idx = obj->available[0];
    obj->stacks[idx][obj->stackSizes[idx]++] = val;
    if (obj->stackSizes[idx] == obj->capacity) heapPop(obj->available, &obj->availSize);
}

int dinnerPlatesPopAtStack(DinnerPlates* obj, int index) {
    if (index < 0 || index >= obj->stacksCount || obj->stackSizes[index] == 0) return -1;
    if (obj->stackSizes[index] == obj->capacity) {
        if (obj->availSize >= obj->availCap) {
            obj->availCap *= 2;
            obj->available = (int*)realloc(obj->available, (size_t)obj->availCap * sizeof(int));
        }
        heapPush(obj->available, &obj->availSize, &obj->availCap, index);
    }
    return obj->stacks[index][--obj->stackSizes[index]];
}

int dinnerPlatesPop(DinnerPlates* obj) {
    while (obj->stacksCount && obj->stackSizes[obj->stacksCount - 1] == 0) {
        free(obj->stacks[obj->stacksCount - 1]);
        obj->stacksCount--;
    }
    if (!obj->stacksCount) return -1;
    return dinnerPlatesPopAtStack(obj, obj->stacksCount - 1);
}

void dinnerPlatesFree(DinnerPlates* obj) {
    if (!obj) return;
    for (int i = 0; i < obj->stacksCount; i++) free(obj->stacks[i]);
    free(obj->stacks); free(obj->stackSizes); free(obj->available); free(obj);
}
