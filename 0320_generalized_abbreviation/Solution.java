// LeetCode 0320 - Generalized Abbreviation

// https://leetcode.com/problems/generalized-abbreviation/



import java.util.ArrayList;

import java.util.List;



class Solution {

    public List<String> generateAbbreviations(String word) {

        List<String> result = new ArrayList<>();

        backtrack(word, 0, "", 0, result);

        return result;

    }



    private void backtrack(String word, int index, String path, int count, List<String> result) {

        if (index == word.length()) {

            result.add(path + (count == 0 ? "" : count));

            return;

        }

        backtrack(word, index + 1, path, count + 1, result);

        String nextPath = path + (count == 0 ? "" : count) + word.charAt(index);

        backtrack(word, index + 1, nextPath, 0, result);

    }

}

