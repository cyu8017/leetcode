// LeetCode 3270 - Find the Key of the Numbers
// https://leetcode.com/problems/find-the-key-of-the-numbers/

int generateKey(int num1, int num2, int num3) {
    int ans = 0, mul = 1;
    for (int t = 0; t < 4; t++) {
        int d = num1 % 10;
        if (num2 % 10 < d) d = num2 % 10;
        if (num3 % 10 < d) d = num3 % 10;
        ans += d * mul;
        mul *= 10;
        num1 /= 10; num2 /= 10; num3 /= 10;
    }
    return ans;
}
