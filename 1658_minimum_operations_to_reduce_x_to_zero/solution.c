// LeetCode 1658 - Minimum Operations to Reduce X to Zero
// https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/

int minOperations(int* nums, int numsSize, int x) {
    long long total = 0;
    for (int i = 0; i < numsSize; i++) total += nums[i];
    long long target = total - x;
    if (target < 0) return -1;
    int best = -1, left = 0;
    long long cur = 0;
    for (int right = 0; right < numsSize; right++) {
        cur += nums[right];
        while (cur > target) cur -= nums[left++];
        if (cur == target) {
            int len = right - left + 1;
            if (len > best) best = len;
        }
    }
    return best < 0 ? -1 : numsSize - best;
}
