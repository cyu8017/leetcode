// LeetCode 0415 - Add Strings

// https://leetcode.com/problems/add-strings/



class Solution {

    public String addStrings(String num1, String num2) {

        int index1 = num1.length() - 1;

        int index2 = num2.length() - 1;

        int carry = 0;

        StringBuilder digits = new StringBuilder();



        while (index1 >= 0 || index2 >= 0 || carry != 0) {

            if (index1 >= 0) {

                carry += num1.charAt(index1) - '0';

                index1--;

            }



            if (index2 >= 0) {

                carry += num2.charAt(index2) - '0';

                index2--;

            }



            digits.append((char) ('0' + carry % 10));

            carry /= 10;

        }



        return digits.reverse().toString();

    }

}
