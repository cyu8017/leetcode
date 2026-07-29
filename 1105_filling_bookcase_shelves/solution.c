// LeetCode 1105 - Filling Bookcase Shelves
// https://leetcode.com/problems/filling-bookcase-shelves/

#include <stdlib.h>

int minHeightShelves(int** books, int booksSize, int* booksColSize, int shelfWidth) {
    (void)booksColSize;
    int* dp = (int*)malloc((size_t)(booksSize + 1) * sizeof(int));
    dp[0] = 0;
    for (int i = 1; i <= booksSize; i++) {
        int width = 0, height = 0;
        dp[i] = 2147483647;
        for (int j = i; j >= 1; j--) {
            width += books[j - 1][0];
            if (width > shelfWidth) break;
            if (books[j - 1][1] > height) height = books[j - 1][1];
            int cand = dp[j - 1] + height;
            if (cand < dp[i]) dp[i] = cand;
        }
    }
    int ans = dp[booksSize];
    free(dp);
    return ans;
}
