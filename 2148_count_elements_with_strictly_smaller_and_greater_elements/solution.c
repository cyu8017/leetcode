// LeetCode 2148 - Count Elements With Strictly Smaller and Greater Elements
// https://leetcode.com/problems/count-elements-with-strictly-smaller-and-greater-elements/

int countElements(int* nums, int numsSize) {
    int mn = nums[0], mx = nums[0];
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] < mn) mn = nums[i];
        if (nums[i] > mx) mx = nums[i];
    }
    int ans = 0;
    for (int i = 0; i < numsSize; i++) if (nums[i] > mn && nums[i] < mx) ans++;
    return ans;
}
