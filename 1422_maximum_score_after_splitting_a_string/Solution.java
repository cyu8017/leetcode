// LeetCode 1422 - Maximum Score After Splitting A String
// https://leetcode.com/problems/maximum-score-after-splitting-a-string/

class Solution {
    public int maxScore(String s) {
        int ones = 0;
        for (char c : s.toCharArray()) if (c == '1') ones++;
        int leftZeros = 0, answer = 0;
        for (int i = 0; i < s.length() - 1; i++) {
            if (s.charAt(i) == '0') leftZeros++;
            else ones--;
            answer = Math.max(answer, leftZeros + ones);
        }
        return answer;
    }
}
