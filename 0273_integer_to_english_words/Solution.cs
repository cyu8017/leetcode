// LeetCode 0273 - Integer to English Words
// https://leetcode.com/problems/integer-to-english-words/

using System.Collections.Generic;

public class Solution {
    private static readonly string[] Ones = {
        "", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
        "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen",
        "Seventeen", "Eighteen", "Nineteen"
    };
    private static readonly string[] Tens = {
        "", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"
    };
    private static readonly string[] Thousands = { "", "Thousand", "Million", "Billion" };

    public string NumberToWords(int num) {
        if (num == 0) {
            return "Zero";
        }

        List<string> parts = new List<string>();
        int chunkIndex = 0;
        while (num > 0) {
            int chunk = num % 1000;
            if (chunk != 0) {
                string chunkWords = ConvertChunk(chunk);
                if (!string.IsNullOrEmpty(Thousands[chunkIndex])) {
                    chunkWords += " " + Thousands[chunkIndex];
                }
                parts.Add(chunkWords);
            }
            num /= 1000;
            chunkIndex++;
        }
        parts.Reverse();
        return string.Join(" ", parts);
    }

    private string ConvertChunk(int value) {
        if (value == 0) {
            return "";
        }
        if (value < 20) {
            return Ones[value];
        }
        if (value < 100) {
            string tens = Tens[value / 10];
            string ones = Ones[value % 10];
            return string.IsNullOrEmpty(ones) ? tens : tens + " " + ones;
        }
        string hundreds = Ones[value / 100];
        string remainder = ConvertChunk(value % 100);
        return string.IsNullOrEmpty(remainder) ? hundreds + " Hundred" : hundreds + " Hundred " + remainder;
    }
}
