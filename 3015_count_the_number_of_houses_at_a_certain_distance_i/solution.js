// LeetCode 3015 - Count the Number of Houses at a Certain Distance I
// https://leetcode.com/problems/count-the-number-of-houses-at-a-certain-distance-i/

var countOfPairs = function(n, x, y) {
    const ans = new Array(n).fill(0);
    x--; y--;
    for (let i = 0; i < n; i++) {
        for (let j = i + 1; j < n; j++) {
            const a = j - i;
            const b = Math.abs(x - i) + Math.abs(y - j) + 1;
            const c = Math.abs(x - j) + Math.abs(y - i) + 1;
            ans[Math.min(a, Math.min(b, c)) - 1] += 2;
        }
    }
    return ans;
};
