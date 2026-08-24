// LeetCode 3017 - Count the Number of Houses at a Certain Distance II
// https://leetcode.com/problems/count-the-number-of-houses-at-a-certain-distance-ii/

var countOfPairs = function(n, x, y) {
    if (x > y) { const t = x; x = y; y = t; }
    const A = new Array(n).fill(0);
    for (let i = 1; i <= n; i++) {
        A[0] += 2;
        A[Math.min(i - 1, Math.abs(i - y) + x)] -= 1;
        A[Math.min(n - i, Math.abs(i - x) + 1 + (n - y))] -= 1;
        A[Math.min(Math.abs(i - x), Math.abs(y - i) + 1)] += 1;
        A[Math.min(Math.abs(i - x) + 1, Math.abs(y - i))] += 1;
        const r = Math.max(x - i, 0) + Math.max(i - y, 0);
        A[r + ((y - x) / 2 | 0)] -= 1;
        A[r + (((y - x + 1) / 2) | 0)] -= 1;
    }
    for (let i = 1; i < n; i++) A[i] += A[i - 1];
    return A;
};
