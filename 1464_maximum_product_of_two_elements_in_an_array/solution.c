// LeetCode 1464 - Maximum Product of Two Elements in an Array
// https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/

int maxProduct(int* nums, int numsSize) {
    int a = 0, b = 0;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] > a) { b = a; a = nums[i]; }
        else if (nums[i] > b) b = nums[i];
    }
    return (a - 1) * (b - 1);
}
