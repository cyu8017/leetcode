// LeetCode 0378 - Kth Smallest Element in a Sorted Matrix
var kthSmallest = function(matrix, k) {
    const rows = matrix.length;
    let left = matrix[0][0];
    let right = matrix[rows - 1][rows - 1];

    while (left < right) {
        const mid = Math.floor((left + right) / 2);
        let count = 0;
        let column = rows - 1;
        for (let row = 0; row < rows; row += 1) {
            while (column >= 0 && matrix[row][column] > mid) column -= 1;
            count += column + 1;
        }
        if (count < k) left = mid + 1;
        else right = mid;
    }

    return left;
};
