// LeetCode 1105 - Filling Bookcase Shelves
// https://leetcode.com/problems/filling-bookcase-shelves/

/**
 * @param {number[][]} books
 * @param {number} shelfWidth
 * @return {number}
 */
var minHeightShelves = function(books, shelfWidth) {
    const n = books.length;
    const dp = Array(n + 1).fill(0);
    for (let i = 1; i <= n; i++) {
        let width = 0, height = 0;
        dp[i] = Infinity;
        for (let j = i; j >= 1; j--) {
            const [w, h] = books[j - 1];
            width += w;
            if (width > shelfWidth) break;
            height = Math.max(height, h);
            dp[i] = Math.min(dp[i], dp[j - 1] + height);
        }
    }
    return dp[n];
};
