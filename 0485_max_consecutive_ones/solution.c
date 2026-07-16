// LeetCode 0485 - Max Consecutive Ones
// https://leetcode.com/problems/max-consecutive-ones/

int findMaxConsecutiveOnes(int* nums, int numsSize) {
    int best = 0;
    int current = 0;
    for (int index = 0; index < numsSize; index++) {
        if (nums[index] == 1) {
            current++;
            if (current > best) {
                best = current;
            }
        } else {
            current = 0;
        }
    }
    return best;
}
