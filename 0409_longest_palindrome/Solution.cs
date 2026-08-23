// LeetCode 0409 - Longest Palindrome

// https://leetcode.com/problems/longest-palindrome/



public class Solution {

    public int LongestPalindrome(string s) {

        int[] counts = new int[128];

        foreach (char character in s) {

            counts[character]++;

        }



        int length = 0;

        bool odd = false;



        foreach (int count in counts) {

            if (count == 0) {

                continue;

            }



            length += count / 2 * 2;



            if (count % 2 == 1) {

                odd = true;

            }

        }



        return length + (odd ? 1 : 0);

    }

}
