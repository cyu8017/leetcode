// LeetCode 1240 - Tiling a Rectangle With the Fewest Squares
// https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares/

#include <stdlib.h>

static void search(int* heights, int m, int n, int used, int* best) {
    if (used >= *best) return;
    int low = heights[0];
    for (int i = 1; i < m; i++) {
        if (heights[i] < low) low = heights[i];
    }
    if (low == n) {
        *best = used;
        return;
    }
    int left = 0;
    while (left < m && heights[left] != low) left++;
    int right = left;
    while (right < m && heights[right] == low) right++;
    int max_size = n - low;
    if (right - left < max_size) max_size = right - left;
    for (int size = max_size; size > 0; size--) {
        for (int i = left; i < left + size; i++) heights[i] = low + size;
        search(heights, m, n, used + 1, best);
        for (int i = left; i < left + size; i++) heights[i] = low;
    }
}

int tilingRectangle(int n, int m) {
    if (n > m) {
        int tmp = n;
        n = m;
        m = tmp;
    }
    int* heights = (int*)calloc((size_t)m, sizeof(int));
    int best = n * m;
    search(heights, m, n, 0, &best);
    free(heights);
    return best;
}
