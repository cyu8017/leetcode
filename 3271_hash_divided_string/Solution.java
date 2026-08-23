// LeetCode 3271 - Hash Divided String
// https://leetcode.com/problems/hash-divided-string/

class Solution {
    public String stringHash(String s, int k) {
        var outSb = new StringBuilder(s.length() / k);
        for (int i = 0; i < s.length(); i += k) {
            int sum = 0;
            for (int j = i; j < i + k; j++) sum += s.charAt(j) - 'a';
            outSb.append((char)('a' + sum % 26));
        }
        return outSb.toString();
    }
}
