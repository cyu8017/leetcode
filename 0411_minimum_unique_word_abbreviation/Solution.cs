// LeetCode 0411 - Minimum Unique Word Abbreviation

// https://leetcode.com/problems/minimum-unique-word-abbreviation/



public class Solution {

    private string target = "";

    private List<string> words = new();

    private int bestLen;

    private string result = "";



    public string MinAbbreviation(string target, IList<string> dictionary) {

        this.target = target;

        this.words = dictionary.Where(word => word.Length == target.Length).ToList();

        bestLen = target.Length + 1;

        result = target;

        Dfs(0, new List<string>(), 0);

        return result;

    }



    private bool Matches(string word, string abbr) {

        int index = 0;

        int pointer = 0;



        while (index < word.Length && pointer < abbr.Length) {

            if (char.IsDigit(abbr[pointer])) {

                if (abbr[pointer] == '0') {

                    return false;

                }



                int number = 0;



                while (pointer < abbr.Length && char.IsDigit(abbr[pointer])) {

                    number = number * 10 + (abbr[pointer] - '0');

                    pointer++;

                }



                index += number;

            } else {

                if (word[index] != abbr[pointer]) {

                    return false;

                }



                index++;

                pointer++;

            }

        }



        return index == word.Length && pointer == abbr.Length;

    }



    private bool Valid(string abbr) {

        if (!Matches(target, abbr)) {

            return false;

        }



        return words.All(word => !Matches(word, abbr));

    }



    private void Dfs(int index, List<string> parts, int skip) {

        if (index == target.Length) {

            string abbr = string.Concat(parts) + (skip != 0 ? skip.ToString() : "");



            if (Valid(abbr)) {

                if (abbr.Length < bestLen || (abbr.Length == bestLen && string.Compare(abbr, result, StringComparison.Ordinal) < 0)) {

                    bestLen = abbr.Length;

                    result = abbr;

                }

            }



            return;

        }



        Dfs(index + 1, parts, skip + 1);



        List<string> newParts = new(parts);



        if (skip != 0) {

            newParts.Add(skip.ToString());

        }



        newParts.Add(target[index].ToString());

        Dfs(index + 1, newParts, 0);

    }

}
