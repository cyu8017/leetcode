// LeetCode 3044 - Most Frequent Prime
// https://leetcode.com/problems/most-frequent-prime/

function isPrime(n) {
    if (n < 2) return false;
    for (let i = 2; i <= (n / i) | 0; i++)
        if (n % i === 0) return false;
    return true;
}
var mostFrequentPrime = function(mat) {
    const m = mat.length, n = mat[0].length;
    const cnt = new Map();
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            for (let a = -1; a <= 1; a++) {
                for (let b = -1; b <= 1; b++) {
                    if (a === 0 && b === 0) continue;
                    let x = i + a, y = j + b, v = mat[i][j];
                    while (x >= 0 && x < m && y >= 0 && y < n) {
                        v = v * 10 + mat[x][y];
                        if (isPrime(v)) {
                            cnt.set(v, (cnt.get(v) || 0) + 1);
                        }
                        x += a;
                        y += b;
                    }
                }
            }
        }
    }
    let ans = -1, mx = 0;
    for (const [key, value] of cnt.entries()) {
        if (mx < value || (mx === value && ans < key)) {
            mx = value;
            ans = key;
        }
    }
    return ans;
};
