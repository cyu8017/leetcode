// LeetCode 2387 - Median of a Row Wise Sorted Matrix
// https://leetcode.com/problems/median-of-a-row-wise-sorted-matrix/

/**
 * @param {number[][]} grid
 * @return {number}
 */
var matrixMedian = function(grid) {
    const m = grid.length, n = grid[0].length;
    let lo = 1, hi = 1000000;
    const need = Math.floor((m * n) / 2) + 1;
    const countLE = (x) => {
        let cnt = 0;
        for (const row of grid) {
            let l = 0, r = n;
            while (l < r) {
                const mid = (l + r) >> 1;
                if (row[mid] <= x) l = mid + 1;
                else r = mid;
            }
            cnt += l;
        }
        return cnt;
    };
    while (lo < hi) {
        const mid = (lo + hi) >> 1;
        if (countLE(mid) >= need) hi = mid;
        else lo = mid + 1;
    }
    return lo;
};
