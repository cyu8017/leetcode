// LeetCode 2355 - Maximum Number of Books You Can Take
// https://leetcode.com/problems/maximum-number-of-books-you-can-take/

/**
 * @param {number[]} books
 * @return {number}
 */
var maximumBooks = function(books) {
    const n = books.length;
    const dp = Array(n).fill(0);
    const stack = [];
    const sum = (l, r, h) => {
        const width = r - l + 1;
        if (h >= width) return width * (2 * h - width + 1) / 2;
        return h * (h + 1) / 2;
    };
    let ans = 0;
    for (let i = 0; i < n; i++) {
        while (stack.length > 0 && books[stack[stack.length - 1]] >= books[i] - (i - stack[stack.length - 1])) {
            stack.pop();
        }
        if (stack.length === 0) {
            dp[i] = sum(0, i, books[i]);
        } else {
            const j = stack[stack.length - 1];
            dp[i] = dp[j] + sum(j + 1, i, books[i]);
        }
        ans = Math.max(ans, dp[i]);
        stack.push(i);
    }
    return ans;
};
