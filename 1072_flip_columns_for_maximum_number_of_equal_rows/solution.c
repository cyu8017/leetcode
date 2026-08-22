// LeetCode 1072 - Flip Columns For Maximum Number of Equal Rows
// https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/

int maxEqualRowsAfterFlips(int** matrix, int matrixSize, int* matrixColSize) {
    int cols = matrixColSize[0];
    int best = 0;
    for (int i = 0; i < matrixSize; i++) {
        int count = 0;
        for (int j = 0; j < matrixSize; j++) {
            int base = matrix[i][0] ^ matrix[j][0];
            int match = 1;
            for (int c = 0; c < cols; c++) {
                if ((matrix[i][c] ^ matrix[j][c]) != base) {
                    match = 0;
                    break;
                }
            }
            if (match) {
                count++;
            }
        }
        if (count > best) {
            best = count;
        }
    }
    return best;
}
