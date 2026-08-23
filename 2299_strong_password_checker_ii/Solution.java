// LeetCode 2299 - Strong Password Checker II
// https://leetcode.com/problems/strong-password-checker-ii/

class Solution {
    public boolean strongPasswordCheckerII(String password) {
        if (password.length() < 8) return false;
        final String special = "!@#$%^&*()-+";
        boolean hasLower = false, hasUpper = false, hasDigit = false, hasSpecial = false;
        for (int i = 0; i < password.length(); i++) {
            char c = password.charAt(i);
            if (i > 0 && c == password.charAt(i - 1)) return false;
            if (c >= 'a' && c <= 'z') hasLower = true;
            else if (c >= 'A' && c <= 'Z') hasUpper = true;
            else if (c >= '0' && c <= '9') hasDigit = true;
            else if (special.indexOf(c) >= 0) hasSpecial = true;
        }
        return hasLower && hasUpper && hasDigit && hasSpecial;
    }
}
