// LeetCode 2535 - Difference Between Element Sum and Digit Sum of an Array
// https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/

int differenceOfSum(int* nums, int numsSize) {
    int elem = 0, digit = 0;
    for (int i = 0; i < numsSize; i++) {
        int x = nums[i];
        elem += x;
        while (x > 0) { digit += x % 10; x /= 10; }
    }
    return elem > digit ? elem - digit : digit - elem;
}
