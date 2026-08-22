// LeetCode 2340 - Minimum Adjacent Swaps to Make a Valid Array
// https://leetcode.com/problems/minimum-adjacent-swaps-to-make-a-valid-array/

int minimumSwaps(int* nums, int numsSize) {
    int minI = 0, maxI = 0;
    for (int i = 1; i < numsSize; i++) {
        if (nums[i] < nums[minI]) minI = i;
        if (nums[i] >= nums[maxI]) maxI = i;
    }
    int ans = minI + (numsSize - 1 - maxI);
    if (minI > maxI) ans--;
    return ans;
}
