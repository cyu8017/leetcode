// LeetCode 1742 - Maximum Number of Balls in a Box
// https://leetcode.com/problems/maximum-number-of-balls-in-a-box/

int countBalls(int lowLimit, int highLimit) {
    int counts[46] = {0};
    for (int value = lowLimit; value <= highLimit; value++) {
        int box = 0;
        int v = value;
        while (v > 0) {
            box += v % 10;
            v /= 10;
        }
        counts[box]++;
    }
    int max = 0;
    for (int i = 0; i < 46; i++) {
        if (counts[i] > max) {
            max = counts[i];
        }
    }
    return max;
}
