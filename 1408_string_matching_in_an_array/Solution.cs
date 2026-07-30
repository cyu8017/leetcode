// LeetCode 1408 - String Matching In An Array
// https://leetcode.com/problems/string-matching-in-an-array/

using System.Collections.Generic;
public class Solution {
    public IList<string> StringMatching(string[] words) {
        var answer = new List<string>();
        for (int i = 0; i < words.Length; i++)
            for (int j = 0; j < words.Length; j++)
                if (i != j && words[j].Contains(words[i])) { answer.Add(words[i]); break; }
        return answer;
    }
}
