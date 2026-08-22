// LeetCode 3982 - Sum of Integers with Maximum Digit Range
// https://leetcode.com/problems/sum-of-integers-with-maximum-digit-range/

int maxDigitRange(int* nums, int numsSize) {
    int mx = 0, ans = 0;
    for (int i = 0; i < numsSize; i++) {
        int x = nums[i];
        int a = 10, b = 0;
        for (int y = x; y > 0; y /= 10) {
            int v = y % 10;
            if (v < a) a = v;
            if (v > b) b = v;
        }
        int r = b - a;
        if (mx < r) {
            mx = r;
            ans = x;
        } else if (mx == r) {
            ans += x;
        }
    }
    return ans;
}
