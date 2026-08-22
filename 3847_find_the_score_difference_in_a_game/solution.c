// LeetCode 3847 - Find The Score Difference In A Game
// https://leetcode.com/problems/find-the-score-difference-in-a-game/

int scoreDifference(int* nums, int numsSize) {
    int ans = 0, k = 1;
    for (int i = 0; i < numsSize; i++) {
        int x = nums[i];
        if (x % 2 != 0) k = -k;
        if (i % 6 == 5) k = -k;
        ans += k * x;
    }
    return ans;
}
