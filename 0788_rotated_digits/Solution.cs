// LeetCode 0788 - Rotated Digits
// https://leetcode.com/problems/rotated-digits/

public class Solution {
    public int RotatedDigits(int n) {
        int count = 0;
        for (int num = 1; num <= n; num++) {
            string s = num.ToString();
            bool ok = true, changed = false;
            foreach (char ch in s) {
                if (ch == '3' || ch == '4' || ch == '7') { ok = false; break; }
                if (ch == '2' || ch == '5' || ch == '6' || ch == '9') changed = true;
            }
            if (ok && changed) count++;
        }
        return count;
    }
}
