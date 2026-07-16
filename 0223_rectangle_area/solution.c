// LeetCode 0223 - Rectangle Area
// https://leetcode.com/problems/rectangle-area/

static int maxInt(int a, int b) {
    return a > b ? a : b;
}

static int minInt(int a, int b) {
    return a < b ? a : b;
}

int computeArea(int ax1, int ay1, int ax2, int ay2, int bx1, int by1, int bx2, int by2) {
    int areaA = (ax2 - ax1) * (ay2 - ay1);
    int areaB = (bx2 - bx1) * (by2 - by1);
    int overlapW = maxInt(0, minInt(ax2, bx2) - maxInt(ax1, bx1));
    int overlapH = maxInt(0, minInt(ay2, by2) - maxInt(ay1, by1));
    return areaA + areaB - overlapW * overlapH;
}
