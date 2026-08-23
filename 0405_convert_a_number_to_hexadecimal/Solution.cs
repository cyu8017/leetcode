// LeetCode 0405 - Convert a Number to Hexadecimal

// https://leetcode.com/problems/convert-a-number-to-hexadecimal/



using System.Text;



public class Solution {

    public string ToHex(int num) {

        if (num == 0) {

            return "0";

        }



        const string digits = "0123456789abcdef";

        uint value = (uint)num;

        StringBuilder result = new();



        while (value > 0) {

            result.Append(digits[(int)(value & 15)]);

            value >>= 4;

        }



        char[] chars = result.ToString().ToCharArray();

        System.Array.Reverse(chars);

        return new string(chars);

    }

}
