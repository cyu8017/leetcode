// LeetCode 3765 - Complete Prime Number
// https://leetcode.com/problems/complete-prime-number/

public class Solution {
    bool IsPrime(int x) {
        if (x < 2) return false;
        for (int i = 2; i * i <= x; i++) if (x % i == 0) return false;
        return true;
    }

    public bool CompletePrime(int num) {
        string s = num.ToString();
        int x = 0;
        foreach (char c in s) {
            x = x * 10 + (c - '0');
            if (!IsPrime(x)) return false;
        }
        x = 0;
        int p = 1;
        for (int i = s.Length - 1; i >= 0; i--) {
            x = p * (s[i] - '0') + x;
            p *= 10;
            if (!IsPrime(x)) return false;
        }
        return true;
    }
}
