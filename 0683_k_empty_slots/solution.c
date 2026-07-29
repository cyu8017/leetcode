// LeetCode 0683 - K Empty Slots
// https://leetcode.com/problems/k-empty-slots/

#include <limits.h>
#include <stdlib.h>

int kEmptySlots(int* bulbs, int bulbsSize, int k) {
    int* days = (int*)malloc((size_t)bulbsSize * sizeof(int));
    for (int day = 0; day < bulbsSize; day++) days[bulbs[day] - 1] = day + 1;
    int ans = INT_MAX;
    int i = 0;
    while (i < bulbsSize - k - 1) {
        int left = i, right = i + k + 1;
        int j = left + 1;
        while (j < right && days[j] > days[left] && days[j] > days[right]) j++;
        if (j == right) {
            int cand = days[left] > days[right] ? days[left] : days[right];
            if (cand < ans) ans = cand;
            i++;
        } else i = j;
    }
    free(days);
    return ans == INT_MAX ? -1 : ans;
}
