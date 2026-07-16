// LeetCode 0045 - Jump Game II
// https://leetcode.com/problems/jump-game-ii/

int jump(int* nums, int numsSize) {
    int jumps = 0;
    int currentEnd = 0;
    int farthest = 0;

    for (int i = 0; i < numsSize - 1; i++) {
        int reach = i + nums[i];
        if (reach > farthest) {
            farthest = reach;
        }
        if (i == currentEnd) {
            jumps++;
            currentEnd = farthest;
        }
    }

    return jumps;
}
