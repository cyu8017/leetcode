// LeetCode 0495 - Teemo Attacking
// https://leetcode.com/problems/teemo-attacking/

int findPoisonedDuration(int* timeSeries, int timeSeriesSize, int duration) {
    if (timeSeriesSize == 0) {
        return 0;
    }
    int total = duration;
    for (int index = 1; index < timeSeriesSize; index++) {
        const int gap = timeSeries[index] - timeSeries[index - 1];
        total += gap < duration ? gap : duration;
    }
    return total;
}
