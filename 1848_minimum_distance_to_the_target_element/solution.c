// LeetCode 1848 - Minimum Distance to the Target Element
// https://leetcode.com/problems/minimum-distance-to-the-target-element/

int getMinDistance(int* nums, int numsSize, int target, int start) {
    int best = numsSize;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] == target) {
            int dist = i >= start ? i - start : start - i;
            if (dist < best) best = dist;
        }
    }
    return best;
}
