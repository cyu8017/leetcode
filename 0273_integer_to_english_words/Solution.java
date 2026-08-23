// LeetCode 0273 - Integer to English Words
// https://leetcode.com/problems/integer-to-english-words/

class Solution {
    private static final String[] ONES = {
        "", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
        "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen",
        "Seventeen", "Eighteen", "Nineteen"
    };
    private static final String[] TENS = {
        "", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"
    };
    private static final String[] THOUSANDS = {"", "Thousand", "Million", "Billion"};

    public String numberToWords(int num) {
        if (num == 0) {
            return "Zero";
        }

        StringBuilder result = new StringBuilder();
        int chunkIndex = 0;
        while (num > 0) {
            int chunk = num % 1000;
            if (chunk != 0) {
                String chunkWords = convertChunk(chunk);
                if (!THOUSANDS[chunkIndex].isEmpty()) {
                    chunkWords += " " + THOUSANDS[chunkIndex];
                }
                if (result.length() > 0) {
                    result.insert(0, " ");
                }
                result.insert(0, chunkWords);
            }
            num /= 1000;
            chunkIndex++;
        }
        return result.toString();
    }

    private String convertChunk(int value) {
        if (value == 0) {
            return "";
        }
        if (value < 20) {
            return ONES[value];
        }
        if (value < 100) {
            String tens = TENS[value / 10];
            String ones = ONES[value % 10];
            return ones.isEmpty() ? tens : tens + " " + ones;
        }
        String hundreds = ONES[value / 100];
        String remainder = convertChunk(value % 100);
        return remainder.isEmpty() ? hundreds + " Hundred" : hundreds + " Hundred " + remainder;
    }
}
