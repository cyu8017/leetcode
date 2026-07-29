// LeetCode 0624 - Maximum Distance in Arrays
// https://leetcode.com/problems/maximum-distance-in-arrays/

static int absInt(int x) {
    return x < 0 ? -x : x;
}

static int maxInt(int a, int b) {
    return a > b ? a : b;
}

static int minInt(int a, int b) {
    return a < b ? a : b;
}

int maxDistance(int** arrays, int arraysSize, int* arraysColSize) {
    int minVal = arrays[0][0];
    int maxVal = arrays[0][arraysColSize[0] - 1];
    int best = 0;
    for (int i = 1; i < arraysSize; i++) {
        int first = arrays[i][0];
        int last = arrays[i][arraysColSize[i] - 1];
        best = maxInt(best, maxInt(absInt(last - minVal), absInt(maxVal - first)));
        minVal = minInt(minVal, first);
        maxVal = maxInt(maxVal, last);
    }
    return best;
}
