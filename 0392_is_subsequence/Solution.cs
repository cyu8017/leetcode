// LeetCode 0392 - Is Subsequence

// https://leetcode.com/problems/is-subsequence/



public class Solution {

    public bool IsSubsequence(string s, string t) {

        int index = 0;



        foreach (char character in t) {

            if (index < s.Length && s[index] == character) {

                index++;

            }

        }



        return index == s.Length;

    }

}
