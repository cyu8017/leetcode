// LeetCode 2299 - Strong Password Checker II
// https://leetcode.com/problems/strong-password-checker-ii/

public class Solution {
    public bool StrongPasswordCheckerII(string password) {
        if (password.Length < 8) return false;
        const string special = "!@#$%^&*()-+";
        bool hasLower = false, hasUpper = false, hasDigit = false, hasSpecial = false;
        for (int i = 0; i < password.Length; i++) {
            char c = password[i];
            if (i > 0 && c == password[i - 1]) return false;
            if (c >= 'a' && c <= 'z') hasLower = true;
            else if (c >= 'A' && c <= 'Z') hasUpper = true;
            else if (c >= '0' && c <= '9') hasDigit = true;
            else if (special.IndexOf(c) >= 0) hasSpecial = true;
        }
        return hasLower && hasUpper && hasDigit && hasSpecial;
    }
}
