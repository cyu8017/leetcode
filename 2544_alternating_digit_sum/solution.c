// LeetCode 2544 - Alternating Digit Sum
// https://leetcode.com/problems/alternating-digit-sum/

int alternateDigitSum(int n) {
    int s[16];
    int len = 0;
    while (n > 0) {
        s[len++] = n % 10;
        n /= 10;
    }
    int ans = 0, sign = 1;
    for (int i = len - 1; i >= 0; i--) {
        ans += sign * s[i];
        sign = -sign;
    }
    return ans;
}
