// LeetCode 0409 - Longest Palindrome

// https://leetcode.com/problems/longest-palindrome/



class Solution {

    public int longestPalindrome(String s) {

        int[] counts = new int[128];

        for (int index = 0; index < s.length(); index++) {

            counts[s.charAt(index)]++;

        }



        int length = 0;

        boolean odd = false;



        for (int count : counts) {

            if (count == 0) {

                continue;

            }



            length += (count / 2) * 2;



            if (count % 2 == 1) {

                odd = true;

            }

        }



        return length + (odd ? 1 : 0);

    }

}
