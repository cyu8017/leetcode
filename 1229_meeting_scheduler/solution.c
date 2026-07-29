// LeetCode 1229 - Meeting Scheduler
// https://leetcode.com/problems/meeting-scheduler/

#include <stdlib.h>

typedef struct {
    int start;
    int end;
} Slot;

static int cmpSlot(const void* a, const void* b) {
    const Slot* x = (const Slot*)a;
    const Slot* y = (const Slot*)b;
    return x->start - y->start;
}

int* minAvailableDuration(int** slots1, int slots1Size, int* slots1ColSize, int** slots2, int slots2Size, int* slots2ColSize, int duration, int* returnSize) {
    (void)slots1ColSize;
    (void)slots2ColSize;
    Slot* s1 = (Slot*)malloc((size_t)slots1Size * sizeof(Slot));
    Slot* s2 = (Slot*)malloc((size_t)slots2Size * sizeof(Slot));
    for (int i = 0; i < slots1Size; i++) {
        s1[i].start = slots1[i][0];
        s1[i].end = slots1[i][1];
    }
    for (int i = 0; i < slots2Size; i++) {
        s2[i].start = slots2[i][0];
        s2[i].end = slots2[i][1];
    }
    qsort(s1, (size_t)slots1Size, sizeof(Slot), cmpSlot);
    qsort(s2, (size_t)slots2Size, sizeof(Slot), cmpSlot);
    int i = 0, j = 0;
    while (i < slots1Size && j < slots2Size) {
        int start = s1[i].start > s2[j].start ? s1[i].start : s2[j].start;
        int end = s1[i].end < s2[j].end ? s1[i].end : s2[j].end;
        if (end - start >= duration) {
            int* ans = (int*)malloc(2 * sizeof(int));
            ans[0] = start;
            ans[1] = start + duration;
            *returnSize = 2;
            free(s1);
            free(s2);
            return ans;
        }
        if (s1[i].end < s2[j].end) i++;
        else j++;
    }
    free(s1);
    free(s2);
    *returnSize = 0;
    return NULL;
}
