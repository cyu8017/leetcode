<?php
// LeetCode 1119 - Remove Vowels From a String
// https://leetcode.com/problems/remove-vowels-from-a-string/

class Solution {
    /**
     * @param String $s
     * @return String
     */
    function removeVowels($s) {
        return preg_replace('/[aeiou]/', '', $s);
    }
}
