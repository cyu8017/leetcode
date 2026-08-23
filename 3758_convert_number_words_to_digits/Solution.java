// LeetCode 3758 - Convert Number Words To Digits
// https://leetcode.com/problems/convert_number_words_to_digits/

class Solution {
    public String convertNumber(String s) {
        String[] d = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
        int n = s.length();
        StringBuilder ans = new StringBuilder();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < 10; j++) {
                int m = d[j].length();
                if (i + m <= n && s.substring(i, i + m).equals(d[j])) {
                    ans.append((char) ('0' + j));
                    i += m - 1;
                    break;
                }
            }
        }
        return ans.toString();
    }
}
