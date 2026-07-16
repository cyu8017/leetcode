// LeetCode 0392 - Is Subsequence

// https://leetcode.com/problems/is-subsequence/



class Solution {

    public boolean isSubsequence(String s, String t) {

        int index = 0;



        for (int charIndex = 0; charIndex < t.length(); charIndex++) {

            if (index < s.length() && s.charAt(index) == t.charAt(charIndex)) {

                index++;

            }

        }



        return index == s.length();

    }

}
