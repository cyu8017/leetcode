// LeetCode 1945 - Sum of Digits of String After Convert
// https://leetcode.com/problems/sum-of-digits-of-string-after-convert/

class Solution {
    public int getLucky(String s, int k) {
        StringBuilder num = new StringBuilder();
        for (int i = 0; i < s.length(); i++) num.append(s.charAt(i) - 'a' + 1);
        String cur = num.toString();
        for (int t = 0; t < k; t++) {
            int sum = 0;
            for (int i = 0; i < cur.length(); i++) sum += cur.charAt(i) - '0';
            cur = String.valueOf(sum);
        }
        return Integer.parseInt(cur);
    }
}
