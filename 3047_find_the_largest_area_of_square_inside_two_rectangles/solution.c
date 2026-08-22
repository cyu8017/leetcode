// LeetCode 3047 - Find the Largest Area of Square Inside Two Rectangles
// https://leetcode.com/problems/find-the-largest-area-of-square-inside-two-rectangles/

static int imin(int a, int b) { return a < b ? a : b; }
static int imax(int a, int b) { return a > b ? a : b; }

long long largestSquareArea(int** bottomLeft, int bottomLeftSize, int* bottomLeftColSize,
                            int** topRight, int topRightSize, int* topRightColSize) {
    (void)bottomLeftColSize; (void)topRight; (void)topRightSize; (void)topRightColSize;
    long long ans = 0;
    for (int i = 0; i < bottomLeftSize; i++) {
        int x1 = bottomLeft[i][0], y1 = bottomLeft[i][1];
        int x2 = topRight[i][0], y2 = topRight[i][1];
        for (int j = i + 1; j < bottomLeftSize; j++) {
            int x3 = bottomLeft[j][0], y3 = bottomLeft[j][1];
            int x4 = topRight[j][0], y4 = topRight[j][1];
            int w = imin(x2, x4) - imax(x1, x3);
            int h = imin(y2, y4) - imax(y1, y3);
            int e = imin(w, h);
            if (e > 0) {
                long long area = (long long)e * e;
                if (area > ans) ans = area;
            }
        }
    }
    return ans;
}
