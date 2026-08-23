// LeetCode 3656 - Determine if a Simple Graph Exists
// https://leetcode.com/problems/determine-if-a-simple-graph-exists/

var simpleGraphExists = function(degrees) {
    const n = degrees.length;
    const d = degrees.slice().sort((a, b) => a - b);
    for (let i = 0, j = n - 1; i < j; i++, j--) {
        const tmp = d[i]; d[i] = d[j]; d[j] = tmp;
    }
    let sum = 0;
    for (const x of d) {
        if (x < 0 || x >= n) return false;
        sum += x;
    }
    if (sum % 2 === 1) return false;
    const prefix = new Array(n + 1).fill(0);
    for (let i = 0; i < n; i++) prefix[i + 1] = prefix[i] + d[i];
    for (let k = 1; k <= n; k++) {
        let right = 0;
        for (let i = k; i < n; i++) right += d[i] < k ? d[i] : k;
        if (prefix[k] > k * (k - 1) + right) return false;
    }
    return true;
};
