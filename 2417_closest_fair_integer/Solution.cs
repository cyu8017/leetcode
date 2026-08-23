// LeetCode 2417 - Closest Fair Integer
// https://leetcode.com/problems/closest-fair-integer/

public class Solution {
    public int ClosestFair(int n) {
        for (int x = n; ; x++) {
            string s = x.ToString();
            if (s.Length % 2 != 0) {
                int p = 1;
                for (int i = 0; i < s.Length; i++) p *= 10;
                return ClosestFair(p);
            }
            int even = 0, odd = 0;
            foreach (char c in s) {
                if ((c - '0') % 2 == 0) even++;
                else odd++;
            }
            if (even == odd) return x;
        }
    }
}
