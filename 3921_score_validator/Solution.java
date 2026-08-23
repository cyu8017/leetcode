// LeetCode 3921 - Score Validator
// https://leetcode.com/problems/score-validator/

class Solution {
    public int[] scoreValidator(String[] events) {
        int score = 0, counter = 0;
        for (String eventStr : events) {
            boolean isNum = eventStr.length() > 0;
            int num = 0;
            int start = 0;
            if (isNum && eventStr.charAt(0) == '-') start = 1;
            for (int i = start; i < eventStr.length(); i++) {
                if (eventStr.charAt(i) < '0' || eventStr.charAt(i) > '9') {
                    isNum = false;
                    break;
                }
                num = num * 10 + (eventStr.charAt(i) - '0');
            }
            if (isNum && !(start == 1 && eventStr.length() == 1)) {
                if (start == 1) num = -num;
                score += num;
            } else if (eventStr.equals("W")) {
                counter++;
                if (counter == 10) break;
            } else {
                score++;
            }
        }
        return new int[] { score, counter };
    }
}
