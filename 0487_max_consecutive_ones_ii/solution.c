// LeetCode 0487 - Max Consecutive Ones II
// https://leetcode.com/problems/max-consecutive-ones-ii/

int findMaxConsecutiveOnes(int* nums, int numsSize) {
    int left = 0;
    int best = 0;
    int zeros = 0;
    for (int right = 0; right < numsSize; right++) {
        if (nums[right] == 0) {
            zeros++;
        }
        while (zeros > 1) {
            if (nums[left] == 0) {
                zeros--;
            }
            left++;
        }
        if (right - left + 1 > best) {
            best = right - left + 1;
        }
    }
    return best;
}
