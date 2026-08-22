// LeetCode 2782 - Number of Unique Categories
// https://leetcode.com/problems/number-of-unique-categories/

#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

int numberOfCategories(int n, int* categoryHandler, int categoryHandlerSize) {
    (void)n;
    bool* seen = (bool*)calloc(n > 0 ? n : 1, sizeof(bool));
    // category ids may be 0..n-1 typically
    int ans = 0;
    // Use simple O(n^2) unique count if values unknown range
    for (int i = 0; i < categoryHandlerSize; i++) {
        bool dup = false;
        for (int j = 0; j < i; j++) {
            if (categoryHandler[j] == categoryHandler[i]) { dup = true; break; }
        }
        if (!dup) ans++;
    }
    free(seen);
    return ans;
}
