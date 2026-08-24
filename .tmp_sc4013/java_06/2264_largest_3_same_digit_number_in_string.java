// LeetCode 2264 - Largest 3-Same-Digit Number in String
// https://leetcode.com/problems/largest-3-same-digit-number-in-string/

class Solution {
    public String largestGoodInteger(String num) {
        String best = "";
        for (int i = 0; i + 2 < num.length(); i++) {
            if (num.charAt(i) == num.charAt(i + 1) && num.charAt(i) == num.charAt(i + 2)) {
                String cand = num.substring(i, i + 3);
                if (cand.compareTo(best) > 0) best = cand;
            }
        }
        return best;
    }
}
