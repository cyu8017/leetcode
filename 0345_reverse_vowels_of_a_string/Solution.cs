// LeetCode 0345 - Reverse Vowels of a String

// https://leetcode.com/problems/reverse-vowels-of-a-string/



public class Solution {

    public string ReverseVowels(string s) {

        char[] chars = s.ToCharArray();

        int left = 0;

        int right = chars.Length - 1;



        while (left < right) {

            while (left < right && !IsVowel(chars[left])) {

                left++;

            }

            while (left < right && !IsVowel(chars[right])) {

                right--;

            }

            (chars[left], chars[right]) = (chars[right], chars[left]);

            left++;

            right--;

        }



        return new string(chars);

    }



    private static bool IsVowel(char ch) {

        return "aeiouAEIOU".Contains(ch);

    }

}
