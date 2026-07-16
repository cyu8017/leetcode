// LeetCode 0502 - IPO
// https://leetcode.com/problems/ipo/

#include <stdlib.h>

typedef struct {
    int capital;
    int profit;
} Project;

typedef struct {
    int value;
} HeapItem;

static int compareProjects(const void* leftPtr, const void* rightPtr) {
    const Project* left = (const Project*)leftPtr;
    const Project* right = (const Project*)rightPtr;
    return left->capital - right->capital;
}

static int compareHeapItems(const void* leftPtr, const void* rightPtr) {
    const HeapItem* left = (const HeapItem*)leftPtr;
    const HeapItem* right = (const HeapItem*)rightPtr;
    return right->value - left->value;
}

static void heapPush(HeapItem* heap, int* heapSize, int value) {
    heap[*heapSize].value = value;
    *heapSize += 1;
    qsort(heap, (size_t)*heapSize, sizeof(HeapItem), compareHeapItems);
}

static int heapPop(HeapItem* heap, int* heapSize) {
    const int top = heap[0].value;
    heap[0] = heap[*heapSize - 1];
    *heapSize -= 1;
    if (*heapSize > 0) {
        qsort(heap, (size_t)*heapSize, sizeof(HeapItem), compareHeapItems);
    }
    return top;
}

int findMaximizedCapital(int k, int w, int* profits, int profitsSize, int* capital, int capitalSize) {
    (void)profitsSize;
    (void)capitalSize;
    Project* projects = (Project*)malloc((size_t)capitalSize * sizeof(Project));
    for (int index = 0; index < capitalSize; index++) {
        projects[index].capital = capital[index];
        projects[index].profit = profits[index];
    }
    qsort(projects, (size_t)capitalSize, sizeof(Project), compareProjects);

    HeapItem heap[50000];
    int heapSize = 0;
    int index = 0;
    for (int round = 0; round < k; round++) {
        while (index < capitalSize && projects[index].capital <= w) {
            heapPush(heap, &heapSize, projects[index].profit);
            index++;
        }
        if (heapSize == 0) {
            break;
        }
        w += heapPop(heap, &heapSize);
    }

    free(projects);
    return w;
}
