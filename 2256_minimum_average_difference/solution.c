// LeetCode 2256 - Minimum Average Difference
// https://leetcode.com/problems/minimum-average-difference/

int minimumAverageDifference(int* nums, int numsSize) {
    long long total = 0;
    for (int i = 0; i < numsSize; i++) total += nums[i];
    long long left = 0;
    long long bestDiff = (1LL << 62);
    int bestIdx = 0;
    for (int i = 0; i < numsSize; i++) {
        left += nums[i];
        long long leftAvg = left / (i + 1);
        long long rightAvg = 0;
        if (i != numsSize - 1) rightAvg = (total - left) / (numsSize - i - 1);
        long long diff = leftAvg - rightAvg;
        if (diff < 0) diff = -diff;
        if (diff < bestDiff) {
            bestDiff = diff;
            bestIdx = i;
        }
    }
    return bestIdx;
}
