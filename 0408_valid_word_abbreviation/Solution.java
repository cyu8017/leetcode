// LeetCode 0408 - Valid Word Abbreviation

// https://leetcode.com/problems/valid-word-abbreviation/



class Solution {

    public boolean validWordAbbreviation(String word, String abbr) {

        int i = 0;

        int j = 0;



        while (i < word.length() && j < abbr.length()) {

            if (Character.isDigit(abbr.charAt(j))) {

                if (abbr.charAt(j) == '0') {

                    return false;

                }



                int number = 0;



                while (j < abbr.length() && Character.isDigit(abbr.charAt(j))) {

                    number = number * 10 + (abbr.charAt(j) - '0');

                    j++;

                }



                i += number;

            } else {

                if (word.charAt(i) != abbr.charAt(j)) {

                    return false;

                }



                i++;

                j++;

            }

        }



        return i == word.length() && j == abbr.length();

    }

}
