// LeetCode 1446 - Consecutive Characters
// https://leetcode.com/problems/consecutive-characters/

class Solution {
    public int maxPower(String s) {
        int answer = 1, run = 1;
        for (int i = 1; i < s.length; i++) {
            run = s[i] == s[i - 1] ? run + 1 : 1;
            answer = Math.max(answer, run);
        }
        return answer;
    }
}
