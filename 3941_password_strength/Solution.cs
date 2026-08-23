// LeetCode 3941 - Password Strength
// https://leetcode.com/problems/password-strength/

using System.Collections.Generic;

public class Solution {
    public int PasswordStrength(string password) {
        var st = new HashSet<char>(password);
        int ans = 0;
        foreach (char ch in st) {
            if (char.IsLower(ch)) ans += 1;
            else if (char.IsUpper(ch)) ans += 2;
            else if (char.IsDigit(ch)) ans += 3;
            else ans += 5;
        }
        return ans;
    }
}
