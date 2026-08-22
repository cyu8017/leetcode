// LeetCode 3745 - Maximize Expression of Three Elements
// https://leetcode.com/problems/maximize-expression-of-three-elements/

int maximizeExpressionOfThree(int* nums, int numsSize) {
    const int inf = 1 << 30;
    int a = -inf, b = -inf, c = inf;
    for (int i = 0; i < numsSize; i++) {
        int x = nums[i];
        if (x < c) c = x;
        if (x >= a) { b = a; a = x; }
        else if (x > b) b = x;
    }
    return a + b - c;
}
