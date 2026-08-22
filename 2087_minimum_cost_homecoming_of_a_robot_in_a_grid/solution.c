// LeetCode 2087 - Minimum Cost Homecoming of a Robot in a Grid
// https://leetcode.com/problems/minimum-cost-homecoming-of-a-robot-in-a-grid/

int minCost(int* startPos, int startPosSize, int* homePos, int homePosSize, int* rowCosts, int rowCostsSize, int* colCosts, int colCostsSize) {
    (void)startPosSize; (void)homePosSize; (void)rowCostsSize; (void)colCostsSize;
    int ans = 0;
    int sr = startPos[0], sc = startPos[1], hr = homePos[0], hc = homePos[1];
    if (sr < hr) for (int r = sr + 1; r <= hr; r++) ans += rowCosts[r];
    else for (int r = sr - 1; r >= hr; r--) ans += rowCosts[r];
    if (sc < hc) for (int c = sc + 1; c <= hc; c++) ans += colCosts[c];
    else for (int c = sc - 1; c >= hc; c--) ans += colCosts[c];
    return ans;
}
