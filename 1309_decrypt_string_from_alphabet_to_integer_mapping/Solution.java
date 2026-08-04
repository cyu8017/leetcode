// LeetCode 1309 - Decrypt String From Alphabet To Integer Mapping
// https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/

class Solution {
    public String freqAlphabets(String s) {
        StringBuilder answer = new StringBuilder();
        int i = s.length() - 1;
        while (i >= 0) {
            if (s.charAt(i) == '#') {
                answer.append((char) (96 + Integer.parseInt(s.substring(i - 2, i))));
                i -= 3;
            } else {
                answer.append((char) (96 + (s.charAt(i) - '0')));
                i -= 1;
            }
        }
        return answer.reverse().toString();
    }
}
