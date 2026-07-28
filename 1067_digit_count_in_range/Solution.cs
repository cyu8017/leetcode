// LeetCode 1067 - Digit Count in Range
// https://leetcode.com/problems/digit-count-in-range/

public class Solution {
    public int DigitsCount(int d, int low, int high) {
        int CountUpto(int n) {
            if (n < 0) {
                return 0;
            }
            string s = n.ToString();
            int length = s.Length;
            int ans = 0;
            for (int i = 0; i < length; i++) {
                int left = i > 0 ? int.Parse(s.Substring(0, i)) : 0;
                int right = i + 1 < length ? int.Parse(s.Substring(i + 1)) : 0;
                int digit = s[i] - '0';
                int power = (int)System.Math.Pow(10, length - i - 1);
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

        return CountUpto(high) - CountUpto(low - 1);
    }
}
