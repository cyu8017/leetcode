// LeetCode 1832 - Check if the Sentence Is Pangram
// https://leetcode.com/problems/check-if-the-sentence-is-pangram/

using System.Collections.Generic;

public class Solution {
    public bool CheckIfPangram(string sentence) {
        return new HashSet<char>(sentence).Count == 26;
    }
}
