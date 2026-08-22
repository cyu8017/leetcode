// LeetCode 2293 - Min Max Game
// https://leetcode.com/problems/min-max-game/

int minMaxGame(int* nums, int numsSize) {
    int n = numsSize;
    while (n > 1) {
        int nextN = n / 2;
        for (int i = 0; i < nextN; i++) {
            if (i % 2 == 0) {
                nums[i] = nums[2 * i] < nums[2 * i + 1] ? nums[2 * i] : nums[2 * i + 1];
            } else {
                nums[i] = nums[2 * i] > nums[2 * i + 1] ? nums[2 * i] : nums[2 * i + 1];
            }
        }
        n = nextN;
    }
    return nums[0];
}
