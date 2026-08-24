// LeetCode 2965 - Find Missing and Repeated Values
// https://leetcode.com/problems/find-missing-and-repeated-values/

var findMissingAndRepeatedValues = function(grid) {
    const n = grid.length;
    const freq = new Array(n * n + 1).fill(0);
    for (let i = 0; i < n; i++)
        for (let j = 0; j < n; j++)
            freq[grid[i][j]]++;
    let rep = 0, miss = 0;
    for (let i = 1; i <= n * n; i++) {
        if (freq[i] === 2) rep = i;
        if (freq[i] === 0) miss = i;
    }
    return [rep, miss];
};
