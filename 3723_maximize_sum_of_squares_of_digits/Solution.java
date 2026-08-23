// LeetCode 3723 - Maximize Sum Of Squares Of Digits
// https://leetcode.com/problems/maximize_sum_of_squares_of_digits/

class Solution {
    public String maxSumOfSquares(int num, int sum) {
        if (num * 9 < sum) return "";
        int k = sum / 9, s = sum % 9;
        StringBuilder ans = new StringBuilder();
        for (int i = 0; i < k; i++) ans.append('9');
        if (s > 0) ans.append((char) ('0' + s));
        while (ans.length() < num) ans.append('0');
        return ans.toString();
    }
}
