// LeetCode 1451 - Rearrange Words In A Sentence
// https://leetcode.com/problems/rearrange-words-in-a-sentence/

using System.Linq;
public class Solution {
    public string ArrangeWords(string text) {
        var words = text.ToLower().Split(' ').OrderBy(w => w.Length).ToArray();
        var s = string.Join(" ", words);
        return char.ToUpper(s[0]) + s.Substring(1);
    }
}
