// LeetCode 0320 - Generalized Abbreviation

// https://leetcode.com/problems/generalized-abbreviation/



using System.Collections.Generic;



public class Solution {

    public IList<string> GenerateAbbreviations(string word) {

        List<string> result = new();

        Backtrack(word, 0, "", 0, result);

        return result;

    }



    private void Backtrack(string word, int index, string path, int count, List<string> result) {

        if (index == word.Length) {

            result.Add(path + (count == 0 ? "" : count.ToString()));

            return;

        }

        Backtrack(word, index + 1, path, count + 1, result);

        string nextPath = path + (count == 0 ? "" : count.ToString()) + word[index];

        Backtrack(word, index + 1, nextPath, 0, result);

    }

}

