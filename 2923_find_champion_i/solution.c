// LeetCode 2923 - Find Champion I
// https://leetcode.com/problems/find-champion-i/

int findChampion(int** grid, int gridSize, int* gridColSize) {
    (void)gridColSize;
    int n = gridSize;
    for (int i = 0; i < n; i++) {
        int win = 1;
        for (int j = 0; j < n; j++) {
            if (i != j && grid[i][j] == 0) { win = 0; break; }
        }
        if (win) return i;
    }
    return -1;
}
