// LeetCode 3417 - Zigzag Grid Traversal With Skip
// https://leetcode.com/problems/zigzag-grid-traversal-with-skip/

var zigzagTraversal = function(grid) {
    const ans = [];
    let skip = false;
    for (let i = 0; i < grid.length; i++) {
        const row = grid[i];
        if (i % 2 === 0) {
            for (const v of row) {
                if (!skip) ans.push(v);
                skip = !skip;
            }
        } else {
            for (let j = row.length - 1; j >= 0; j--) {
                if (!skip) ans.push(row[j]);
                skip = !skip;
            }
        }
    }
    return ans;
};
