// LeetCode 0831 - Masking Personal Information
// https://leetcode.com/problems/masking-personal-information/

class Solution {
    public String maskPII(String s) {
        int at = s.indexOf('@');
        if (at >= 0) {
            s = s.toLowerCase();
            at = s.indexOf('@');
            String name = s.substring(0, at);
            String domain = s.substring(at + 1);
            return name.charAt(0) + "*****" + name.charAt(name.length() - 1) + "@" + domain;
        }
        StringBuilder digits = new StringBuilder();
        for (char ch : s.toCharArray()) if (Character.isDigit(ch)) digits.append(ch);
        String local = digits.substring(digits.length() - 4);
        int country = digits.length() - 10;
        if (country == 0) return "***-***-" + local;
        return "+" + "*".repeat(country) + "-***-***-" + local;
    }
}
