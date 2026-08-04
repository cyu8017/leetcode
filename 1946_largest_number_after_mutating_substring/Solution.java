// LeetCode 1946 - Largest Number After Mutating Substring
// https://leetcode.com/problems/largest-number-after-mutating-substring/

class Solution {
    public String maximumNumber(String num, int[] change) {
        char[] chars = num.toCharArray();
        boolean started = false;
        for (int i = 0; i < chars.length; i++) {
            int d = chars[i] - '0';
            int mapped = change[d];
            if (mapped > d) {
                chars[i] = (char) ('0' + mapped);
                started = true;
            } else if (mapped < d && started) break;
        }
        return new String(chars);
    }
}
