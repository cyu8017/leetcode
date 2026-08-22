// LeetCode 3012 - Minimize Length of Array Using Operations
// https://leetcode.com/problems/minimize-length-of-array-using-operations/

int minimumArrayLength(int* nums, int numsSize) {
    int mi = nums[0];
    for (int i = 1; i < numsSize; i++) if (nums[i] < mi) mi = nums[i];
    int cnt = 0;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] % mi != 0) return 1;
        if (nums[i] == mi) cnt++;
    }
    return (cnt + 1) / 2;
}
