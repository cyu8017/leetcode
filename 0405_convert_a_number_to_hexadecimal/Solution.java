// LeetCode 0405 - Convert a Number to Hexadecimal

// https://leetcode.com/problems/convert-a-number-to-hexadecimal/



class Solution {

    public String toHex(int num) {

        if (num == 0) {

            return "0";

        }



        String digits = "0123456789abcdef";

        long value = num & 0xffffffffL;

        StringBuilder result = new StringBuilder();



        while (value > 0) {

            result.append(digits.charAt((int) (value & 15)));

            value >>= 4;

        }



        return result.reverse().toString();

    }

}
