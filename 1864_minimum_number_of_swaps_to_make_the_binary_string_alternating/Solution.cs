// LeetCode 1864 - Minimum Number of Swaps to Make the Binary String Alternating
// https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-binary-string-alternating/

public class Solution {
    public int MinSwaps(string s) {
        int zeros = 0;
        foreach (char ch in s) {
            if (ch == '0') {
                zeros++;
            }
        }
        int ones = s.Length - zeros;
        if (Math.Abs(zeros - ones) > 1) {
            return -1;
        }

        int Mismatches(char start) {
            int count = 0;
            for (int i = 0; i < s.Length; i++) {
                char expected = i % 2 == 0 ? start : (start == '0' ? '1' : '0');
                if (s[i] != expected) {
                    count++;
                }
            }
            return count / 2;
        }

        if (zeros == ones) {
            return Math.Min(Mismatches('0'), Mismatches('1'));
        }
        return zeros > ones ? Mismatches('0') : Mismatches('1');
    }
}
