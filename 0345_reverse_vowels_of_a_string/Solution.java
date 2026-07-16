// LeetCode 0345 - Reverse Vowels of a String

// https://leetcode.com/problems/reverse-vowels-of-a-string/



class Solution {

    public String reverseVowels(String s) {

        char[] chars = s.toCharArray();

        int left = 0;

        int right = chars.length - 1;



        while (left < right) {

            while (left < right && !isVowel(chars[left])) {

                left++;

            }

            while (left < right && !isVowel(chars[right])) {

                right--;

            }

            char temp = chars[left];

            chars[left] = chars[right];

            chars[right] = temp;

            left++;

            right--;

        }



        return new String(chars);

    }



    private boolean isVowel(char ch) {

        return ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u'

            || ch == 'A' || ch == 'E' || ch == 'I' || ch == 'O' || ch == 'U';

    }

}
