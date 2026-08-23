// LeetCode 2718 - Sum of Matrix After Queries
// https://leetcode.com/problems/sum-of-matrix-after-queries/

var matrixSumQueries = function(n, queries) {
    const rowDone = new Array(n).fill(false);
    const colDone = new Array(n).fill(false);
    let rowsLeft = n, colsLeft = n;
    let ans = 0;
    for (let i = queries.length - 1; i >= 0; i--) {
        const type = queries[i][0], idx = queries[i][1], val = queries[i][2];
        if (type === 0) {
            if (!rowDone[idx]) {
                ans += val * colsLeft;
                rowDone[idx] = true;
                rowsLeft--;
            }
        } else {
            if (!colDone[idx]) {
                ans += val * rowsLeft;
                colDone[idx] = true;
                colsLeft--;
            }
        }
    }
    return ans;
};
