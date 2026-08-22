// LeetCode 0406 - Queue Reconstruction by Height
// https://leetcode.com/problems/queue-reconstruction-by-height/

#include <stdlib.h>

typedef struct {
    int height;
    int ahead;
} Person;

static int compare_people(const void* left, const void* right) {
    const Person* a = (const Person*)left;
    const Person* b = (const Person*)right;

    if (a->height != b->height) {
        return b->height - a->height;
    }
    return a->ahead - b->ahead;
}

static void queue_insert(int** queue, int* queueSize, int insertIndex, int height, int ahead) {
    *queueSize += 1;
    *queue = (int**)realloc(*queue, (size_t)(*queueSize) * sizeof(int*));

    for (int index = *queueSize - 1; index > insertIndex; index--) {
        (*queue)[index] = (*queue)[index - 1];
    }

    (*queue)[insertIndex] = (int*)malloc(2 * sizeof(int));
    (*queue)[insertIndex][0] = height;
    (*queue)[insertIndex][1] = ahead;
}

int** reconstructQueue(int** people, int peopleSize, int* peopleColSize, int* returnSize, int** returnColumnSizes) {
    (void)peopleColSize;

    Person* sorted = (Person*)malloc((size_t)peopleSize * sizeof(Person));
    for (int index = 0; index < peopleSize; index++) {
        sorted[index].height = people[index][0];
        sorted[index].ahead = people[index][1];
    }

    qsort(sorted, (size_t)peopleSize, sizeof(Person), compare_people);

    int** queue = NULL;
    *returnSize = 0;
    for (int index = 0; index < peopleSize; index++) {
        queue_insert(&queue, returnSize, sorted[index].ahead, sorted[index].height, sorted[index].ahead);
    }

    *returnColumnSizes = (int*)malloc((size_t)(*returnSize) * sizeof(int));
    for (int index = 0; index < *returnSize; index++) {
        (*returnColumnSizes)[index] = 2;
    }

    free(sorted);
    return queue;
}
