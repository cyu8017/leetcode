// LeetCode 0408 - Valid Word Abbreviation

// https://leetcode.com/problems/valid-word-abbreviation/



public class Solution {

    public bool ValidWordAbbreviation(string word, string abbr) {

        int i = 0;

        int j = 0;



        while (i < word.Length && j < abbr.Length) {

            if (char.IsDigit(abbr[j])) {

                if (abbr[j] == '0') {

                    return false;

                }



                int number = 0;



                while (j < abbr.Length && char.IsDigit(abbr[j])) {

                    number = number * 10 + (abbr[j] - '0');

                    j++;

                }



                i += number;

            } else {

                if (word[i] != abbr[j]) {

                    return false;

                }



                i++;

                j++;

            }

        }



        return i == word.Length && j == abbr.Length;

    }

}
