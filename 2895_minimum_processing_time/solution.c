// LeetCode 2895 - Minimum Processing Time
// https://leetcode.com/problems/minimum-processing-time/

#include <stdlib.h>

static int cmp_asc(const void* a, const void* b) { return (*(const int*)a) - (*(const int*)b); }
static int cmp_desc(const void* a, const void* b) { return (*(const int*)b) - (*(const int*)a); }

int minProcessingTime(int* processorTime, int processorTimeSize, int* tasks, int tasksSize) {
    (void)tasksSize;
    qsort(processorTime, processorTimeSize, sizeof(int), cmp_asc);
    qsort(tasks, tasksSize, sizeof(int), cmp_desc);
    int ans = 0;
    for (int i = 0; i < processorTimeSize; i++) {
        int fin = processorTime[i] + tasks[i * 4];
        if (fin > ans) ans = fin;
    }
    return ans;
}
