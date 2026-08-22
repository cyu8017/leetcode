// LeetCode 2244 - Minimum Rounds to Complete All Tasks
// https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/

#include <stdlib.h>

static int cmp_int(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

int minimumRounds(int* tasks, int tasksSize) {
    qsort(tasks, (size_t)tasksSize, sizeof(int), cmp_int);
    int ans = 0;
    int i = 0;
    while (i < tasksSize) {
        int j = i;
        while (j < tasksSize && tasks[j] == tasks[i]) j++;
        int c = j - i;
        if (c == 1) return -1;
        ans += (c + 2) / 3;
        i = j;
    }
    return ans;
}
