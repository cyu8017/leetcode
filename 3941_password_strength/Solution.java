// LeetCode 3941 - Password Strength
// https://leetcode.com/problems/password-strength/

import java.util.HashSet;
import java.util.Set;

class Solution {
    public int passwordStrength(String password) {
        Set<Character> st = new HashSet<>();
        for (int i = 0; i < password.length(); i++) st.add(password.charAt(i));
        int ans = 0;
        for (char ch : st) {
            if (Character.isLowerCase(ch)) ans += 1;
            else if (Character.isUpperCase(ch)) ans += 2;
            else if (Character.isDigit(ch)) ans += 3;
            else ans += 5;
        }
        return ans;
    }
}
