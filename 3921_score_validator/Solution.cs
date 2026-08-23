// LeetCode 3921 - Score Validator
// https://leetcode.com/problems/score-validator/

public class Solution {
    public int[] ScoreValidator(string[] events) {
        int score = 0, counter = 0;
        foreach (var eventStr in events) {
            bool isNum = eventStr.Length > 0;
            int num = 0;
            int start = 0;
            if (isNum && eventStr[0] == '-') start = 1;
            for (int i = start; i < eventStr.Length; i++) {
                if (eventStr[i] < '0' || eventStr[i] > '9') {
                    isNum = false;
                    break;
                }
                num = num * 10 + (eventStr[i] - '0');
            }
            if (isNum && !(start == 1 && eventStr.Length == 1)) {
                if (start == 1) num = -num;
                score += num;
            } else if (eventStr == "W") {
                counter++;
                if (counter == 10) break;
            } else {
                score++;
            }
        }
        return new int[] { score, counter };
    }
}
