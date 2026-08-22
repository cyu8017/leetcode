// LeetCode 2216 - Minimum Deletions to Make Array Beautiful
// https://leetcode.com/problems/minimum-deletions-to-make-array-beautiful/

int minDeletion(int* nums, int numsSize) {
    int ans = 0, i = 0;
    while (i + 1 < numsSize) {
        if (nums[i] == nums[i + 1]) { ans++; i++; }
        else i += 2;
    }
    if ((numsSize - ans) % 2 == 1) ans++;
    return ans;
}
