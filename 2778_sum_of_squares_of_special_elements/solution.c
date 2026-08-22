// LeetCode 2778 - Sum of Squares of Special Elements
// https://leetcode.com/problems/sum-of-squares-of-special-elements/

int sumOfSquares(int* nums, int numsSize) {
    int ans = 0;
    for (int i = 0; i < numsSize; i++) {
        if (numsSize % (i + 1) == 0) {
            ans += nums[i] * nums[i];
        }
    }
    return ans;
}
