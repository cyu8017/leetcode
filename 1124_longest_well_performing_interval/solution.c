// LeetCode 1124 - Longest Well-Performing Interval
// https://leetcode.com/problems/longest-well-performing-interval/

#include <stdlib.h>
#include <string.h>

int longestWPI(int* hours, int hoursSize) {
    int offset = hoursSize;
    int* first = (int*)malloc((size_t)(2 * hoursSize + 5) * sizeof(int));
    for (int i = 0; i < 2 * hoursSize + 5; i++) first[i] = -2;
    first[offset] = -1;
    int score = 0, ans = 0;
    for (int i = 0; i < hoursSize; i++) {
        score += hours[i] > 8 ? 1 : -1;
        if (score > 0) ans = i + 1;
        else {
            int key = score - 1 + offset;
            if (key >= 0 && key < 2 * hoursSize + 5 && first[key] != -2) {
                int cand = i - first[key];
                if (cand > ans) ans = cand;
            }
        }
        int k = score + offset;
        if (first[k] == -2) first[k] = i;
    }
    free(first);
    return ans;
}
