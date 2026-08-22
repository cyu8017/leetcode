// LeetCode 0643 - Maximum Average Subarray I
// https://leetcode.com/problems/maximum-average-subarray-i/

double findMaxAverage(int* nums, int numsSize, int k) {
    double window = 0;
    for (int i = 0; i < k; i++) {
        window += nums[i];
    }
    double best = window;
    for (int i = k; i < numsSize; i++) {
        window += nums[i] - nums[i - k];
        if (window > best) {
            best = window;
        }
    }
    return best / k;
}
