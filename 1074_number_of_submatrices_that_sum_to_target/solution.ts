// LeetCode 1074 - Number of Submatrices That Sum to Target
// https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/

function numSubmatrixSumTarget(matrix: number[][], target: number): number {
    const rows = matrix.length;
    const cols = matrix[0].length;
    let ans = 0;
    for (let left = 0; left < cols; left++) {
        const rowSum = new Array(rows).fill(0);
        for (let right = left; right < cols; right++) {
            for (let r = 0; r < rows; r++) rowSum[r] += matrix[r][right];
            let prefix = 0;
            const seen = new Map<number, number>([[0, 1]]);
            for (const val of rowSum) {
                prefix += val;
                ans += seen.get(prefix - target) || 0;
                seen.set(prefix, (seen.get(prefix) || 0) + 1);
            }
        }
    }
    return ans;
}
