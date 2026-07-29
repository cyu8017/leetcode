// LeetCode 1402 - Reducing Dishes
// https://leetcode.com/problems/reducing-dishes/

#include <stdlib.h>

static int cmp_desc(const void* a, const void* b) { return *(const int*)b - *(const int*)a; }

int maxSatisfaction(int* satisfaction, int satisfactionSize) {
    qsort(satisfaction, satisfactionSize, sizeof(int), cmp_desc);
    int total = 0, answer = 0;
    for (int i = 0; i < satisfactionSize; i++) {
        if (total + satisfaction[i] <= 0) break;
        total += satisfaction[i];
        answer += total;
    }
    return answer;
}
