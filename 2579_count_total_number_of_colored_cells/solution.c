// LeetCode 2579 - Count Total Number of Colored Cells
// https://leetcode.com/problems/count-total-number-of-colored-cells/

long long coloredCells(int n) {
    return 1 + 2LL * n * (n - 1);
}
