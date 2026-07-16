// LeetCode 0311 - Sparse Matrix Multiplication
export function multiply(mat1: number[][], mat2: number[][]): number[][] {
    const rows = mat1.length;
    const inner = mat1[0].length;
    const cols = mat2[0].length;
    const result = Array.from({ length: rows }, () => Array(cols).fill(0));
    for (let row = 0; row < rows; row += 1) {
        for (let index = 0; index < inner; index += 1) {
            if (mat1[row][index] === 0) continue;
            for (let col = 0; col < cols; col += 1) {
                if (mat2[index][col] !== 0) {
                    result[row][col] += mat1[row][index] * mat2[index][col];
                }
            }
        }
    }
    return result;
}
