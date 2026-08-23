// LeetCode 0389 - Find the Difference

// https://leetcode.com/problems/find-the-difference/



public class Solution {

    public char FindTheDifference(string s, string t) {

        int xorValue = 0;

        foreach (char ch in s) {

            xorValue ^= ch;

        }

        foreach (char ch in t) {

            xorValue ^= ch;

        }

        return (char)xorValue;

    }

}
