// LeetCode 2259 - Remove Digit From Number to Maximize Result
// https://leetcode.com/problems/remove-digit-from-number-to-maximize-result/

class Solution {
    public String removeDigit(String number, char digit) {
        String best = "";
        for (int i = 0; i < number.length(); i++) {
            if (number.charAt(i) == digit) {
                String cand = number.substring(0, i) + number.substring(i + 1);
                if (cand.compareTo(best) > 0) best = cand;
            }
        }
        return best;
    }
}
