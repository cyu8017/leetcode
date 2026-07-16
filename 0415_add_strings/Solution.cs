// LeetCode 0415 - Add Strings

// https://leetcode.com/problems/add-strings/



public class Solution {

    public string AddStrings(string num1, string num2) {

        int index1 = num1.Length - 1;

        int index2 = num2.Length - 1;

        int carry = 0;

        List<char> digits = new();



        while (index1 >= 0 || index2 >= 0 || carry != 0) {

            if (index1 >= 0) {

                carry += num1[index1] - '0';

                index1--;

            }



            if (index2 >= 0) {

                carry += num2[index2] - '0';

                index2--;

            }



            digits.Add((char)('0' + carry % 10));

            carry /= 10;

        }



        digits.Reverse();

        return new string(digits.ToArray());

    }

}
