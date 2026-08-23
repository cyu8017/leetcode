// LeetCode 0389 - Find the Difference

// https://leetcode.com/problems/find-the-difference/



class Solution {

    public char findTheDifference(String s, String t) {

        int xorValue = 0;

        for (int index = 0; index < s.length(); index++) {

            xorValue ^= s.charAt(index);

        }

        for (int index = 0; index < t.length(); index++) {

            xorValue ^= t.charAt(index);

        }

        return (char) xorValue;

    }

}
