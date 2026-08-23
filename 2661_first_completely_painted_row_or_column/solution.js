// LeetCode 2661 - First Completely Painted Row or Column
// https://leetcode.com/problems/first-completely-painted-row-or-column/

var firstCompleteIndex = function(arr, mat) {
    const m = mat.length, n = mat[0].length;
    const posR = new Array(m * n + 1), posC = new Array(m * n + 1);
    for (let i = 0; i < m; i++)
        for (let j = 0; j < n; j++) {
            posR[mat[i][j]] = i;
            posC[mat[i][j]] = j;
        }
    const rowCnt = new Array(m).fill(0), colCnt = new Array(n).fill(0);
    for (let i = 0; i < arr.length; i++) {
        const r = posR[arr[i]], c = posC[arr[i]];
        rowCnt[r]++;
        colCnt[c]++;
        if (rowCnt[r] === n || colCnt[c] === m) return i;
    }
    return -1;
};
