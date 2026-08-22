// LeetCode 3096 - Minimum Levels to Gain More Points
// https://leetcode.com/problems/minimum-levels-to-gain-more-points/

int minimumLevels(int* possible, int possibleSize) {
    int s = 0;
    for (int i = 0; i < possibleSize; i++) s += possible[i] == 0 ? -1 : 1;
    int t = 0;
    for (int i = 0; i < possibleSize - 1; i++) {
        t += possible[i] == 0 ? -1 : 1;
        if (t > s - t) return i + 1;
    }
    return -1;
}
