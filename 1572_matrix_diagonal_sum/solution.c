// LeetCode 1572 - Matrix Diagonal Sum
// https://leetcode.com/problems/matrix-diagonal-sum/

int diagonalSum(int** mat, int matSize, int* matColSize) {
    (void)matColSize;
    int n = matSize, ans = 0;
    for (int i = 0; i < n; i++) {
        ans += mat[i][i] + mat[i][n - 1 - i];
    }
    if (n % 2) ans -= mat[n / 2][n / 2];
    return ans;
}
