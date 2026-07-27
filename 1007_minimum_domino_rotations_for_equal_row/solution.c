// LeetCode 1007 - Minimum Domino Rotations For Equal Row
// https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/

static int check_domino(int* tops, int* bottoms, int n, int target) {
    int rotTop = 0, rotBot = 0;
    for (int i = 0; i < n; i++) {
        if (tops[i] != target && bottoms[i] != target) return -1;
        if (tops[i] != target) rotTop++;
        if (bottoms[i] != target) rotBot++;
    }
    return rotTop < rotBot ? rotTop : rotBot;
}

int minDominoRotations(int* tops, int topsSize, int* bottoms, int bottomsSize) {
    (void)bottomsSize;
    int a = check_domino(tops, bottoms, topsSize, tops[0]);
    int b = check_domino(tops, bottoms, topsSize, bottoms[0]);
    if (a < 0) return b;
    if (b < 0) return a;
    return a < b ? a : b;
}
