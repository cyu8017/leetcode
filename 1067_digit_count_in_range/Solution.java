// LeetCode 1067 - Digit Count in Range
// https://leetcode.com/problems/digit-count-in-range/

class Solution {
    public int digitsCount(int d, int low, int high) {
        return countUpto(high, d) - countUpto(low - 1, d);
    }

    private int countUpto(int n, int d) {
        if (n < 0) {
            return 0;
        }
        String s = String.valueOf(n);
        int length = s.length();
        int ans = 0;
        for (int i = 0; i < length; i++) {
            int left = i > 0 ? Integer.parseInt(s.substring(0, i)) : 0;
            int right = i + 1 < length ? Integer.parseInt(s.substring(i + 1)) : 0;
            int digit = s.charAt(i) - '0';
            int power = pow10(length - i - 1);
            if (d != 0) {
                ans += left * power;
                if (digit > d) {
                    ans += power;
                } else if (digit == d) {
                    ans += right + 1;
                }
            } else {
                if (i == 0) {
                    continue;
                }
                ans += (left - 1) * power;
                if (digit > 0) {
                    ans += power;
                } else {
                    ans += right + 1;
                }
            }
        }
        return ans;
    }

    private int pow10(int n) {
        int p = 1;
        for (int i = 0; i < n; i++) {
            p *= 10;
        }
        return p;
    }
}
