// LeetCode 3933 - Largest Local Values in a Matrix II
// https://leetcode.com/problems/largest-local-values-in-a-matrix-ii/
var countLocalMaximums = function(matrix) {
        let rows = matrix.length, cols = matrix[0].length;
        let positions = Array.from({length: 201}, () => []);
        for (let i = 0; i < 201; i++) positions[i] = [];
        for (let row = 0; row < rows; row++) {
            for (let col = 0; col < cols; col++) {
                let value = matrix[row][col];
                if (value > 0) positions[value].push([ row, col ]);
            }
        }
        let answer = 0;
        for (let value = 1; value <= 200; value++) {
            if (positions[value].length === 0) continue;
            let prefix = new Array(rows + 1).fill(0)[cols + 1];
            for (let row = 0; row < rows; row++) {
                for (let col = 0; col < cols; col++) {
                    let add = matrix[row][col] > value ? 1 : 0;
                    prefix[row + 1][col + 1] = prefix[row][col + 1] + prefix[row + 1][col] - prefix[row][col] + add;
                }
            }
            for (const pos of positions[value]) {
                let row = pos[0], col = pos[1];
                let top = Math.max(0, row - value), bottom = Math.min(rows - 1, row + value);
                let left = Math.max(0, col - value), right = Math.min(cols - 1, col + value);
                let greater = prefix[bottom + 1][right + 1] - prefix[top][right + 1] - prefix[bottom + 1][left] + prefix[top][left];
                for (const dr of [ -value, value ]) {
                    for (const dc of [ -value, value ]) {
                        let rr = row + dr, cc = col + dc;
                        if (rr >= 0 && rr < rows && cc >= 0 && cc < cols && matrix[rr][cc] > value) greater--;
                    }
                }
                if (greater == 0) answer++;
            }
        }
        return answer;
    
};
