// LeetCode 3602 - Hexadecimal and Hexatrigesimal Conversion
// https://leetcode.com/problems/hexadecimal-and-hexatrigesimal-conversion/

class Solution {
    String f(int x, int k) {
        StringBuilder res = new StringBuilder();
        while (x > 0) {
            int v = x % k;
            res.append(v <= 9 ? (char) ('0' + v) : (char) ('A' + v - 10));
            x /= k;
        }
        return res.reverse().toString();
    }

    public String concatHex36(int n) {
        return f(n * n, 16) + f(n * n * n, 36);
    }
}
