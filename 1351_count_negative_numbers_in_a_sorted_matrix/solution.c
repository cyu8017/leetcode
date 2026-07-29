// LeetCode 1351 - Count Negative Numbers in a Sorted Matrix
// https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/

int countNegatives(int** grid, int gridSize, int* gridColSize) {
    int ans = 0;
    for (int r = 0; r < gridSize; r++) {
        int n = gridColSize[r];
        int lo = 0, hi = n;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (grid[r][mid] < 0) hi = mid;
            else lo = mid + 1;
        }
        ans += n - lo;
    }
    return ans;
}
