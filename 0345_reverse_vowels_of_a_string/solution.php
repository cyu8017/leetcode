<?php
// LeetCode 0345 - Reverse Vowels of a String
// https://leetcode.com/problems/reverse-vowels-of-a-string/

class Solution {
    /**
     * @param String $s
     * @return String
     */
    function reverseVowels($s) {
        return $this->reverse_vowels($s);
    }

    /**
     * @param String $s
     * @return String
     */
    function reverse_vowels($s) {
        $vowels = "aeiouAEIOU";
        $chars = str_split($s);
        $left = 0;
        $right = count($chars) - 1;

        while ($left < $right) {
            while ($left < $right && strpos($vowels, $chars[$left]) === false) {
                $left++;
            }
            while ($left < $right && strpos($vowels, $chars[$right]) === false) {
                $right--;
            }
            [$chars[$left], $chars[$right]] = [$chars[$right], $chars[$left]];
            $left++;
            $right--;
        }

        return implode("", $chars);
    }
}
