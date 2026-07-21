// LeetCode 1822 - Sign of the Product of an Array
// https://leetcode.com/problems/sign-of-the-product-of-an-array/

int arraySign(int* nums, int numsSize) {
    int sign = 1;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] == 0) return 0;
        if (nums[i] < 0) sign = -sign;
    }
    return sign;
}
