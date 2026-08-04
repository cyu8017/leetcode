// LeetCode 1408 - String Matching In An Array
// https://leetcode.com/problems/String-matching-in-an-array/

import java.util.*;

class Solution {
    public List<String> stringMatching(String[] words) {
        var answer = new ArrayList<>();
        for (int i = 0; i < words.length; i++)
            for (int j = 0; j < words.length; j++)
                if (i != j && words[j].contains(words[i])) { answer.add(words[i]); break; }
        return answer;
    }
}
