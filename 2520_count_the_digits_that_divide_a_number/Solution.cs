// LeetCode 2520 - Count the Digits That Divide a Number
// https://leetcode.com/problems/count-the-digits-that-divide-a-number/

public class Solution {
    public int CountDigits(int num) {
        int ans = 0, x = num;
        while (x > 0) {
            int d = x % 10;
            if (d != 0 && num % d == 0) ans++;
            x /= 10;
        }
        return ans;
    }
}
