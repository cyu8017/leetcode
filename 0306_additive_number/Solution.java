// LeetCode 0306 - Additive Number
// https://leetcode.com/problems/additive-number/

class Solution {
    public boolean isAdditiveNumber(String num) {
        for (int firstEnd = 1; firstEnd < num.length(); firstEnd++) {
            for (int secondEnd = firstEnd + 1; secondEnd < num.length(); secondEnd++) {
                if (valid(num, num.substring(0, firstEnd), num.substring(firstEnd, secondEnd), secondEnd)) {
                    return true;
                }
            }
        }
        return false;
    }

    private boolean valid(String num, String first, String second, int start) {
        if ((first.length() > 1 && first.charAt(0) == '0')
                || (second.length() > 1 && second.charAt(0) == '0')) {
            return false;
        }
        while (start < num.length()) {
            String total = addStrings(first, second);
            if (!num.startsWith(total, start)) {
                return false;
            }
            first = second;
            second = total;
            start += total.length();
        }
        return true;
    }

    private String addStrings(String left, String right) {
        return String.valueOf(Long.parseLong(left) + Long.parseLong(right));
    }
}
