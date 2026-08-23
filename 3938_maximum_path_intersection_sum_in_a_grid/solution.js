// LeetCode 3938 - Maximum Path Intersection Sum in a Grid
// https://leetcode.com/problems/maximum-path-intersection-sum-in-a-grid/

var maxPathSum = function(grid) {
    const rows = grid.length, cols = grid[0].length;
    let answer = -2147483648;
    for (let row = 0; row < rows; row++) {
        const r = row;
        answer = Math.max(answer, checkLine(cols, (col) => grid[r][col]));
    }
    for (let col = 0; col < cols; col++) {
        const c = col;
        answer = Math.max(answer, checkLine(rows, (row) => grid[row][c]));
    }
    for (let row = 1; row + 1 < rows; row++) {
        for (let col = 1; col + 1 < cols; col++) {
            if (grid[row][col] > answer) answer = grid[row][col];
        }
    }
    return answer;
};

function checkLine(length, value) {
    let answer = -2147483648;
    let bestEnding = value(0) + value(1);
    if (bestEnding > answer) answer = bestEnding;
    for (let i = 2; i < length; i++) {
        if (value(i - 1) + value(i) > bestEnding + value(i)) bestEnding = value(i - 1) + value(i);
        else bestEnding += value(i);
        if (bestEnding > answer) answer = bestEnding;
    }
    return answer;
}
