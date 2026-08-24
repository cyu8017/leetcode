<?php
// LeetCode 3856 - Trim Trailing Vowels
// https://leetcode.com/problems/trim-trailing-vowels/

class Solution {
    function isVowel($c) {
        return $c === 'a' || $c === 'e' || $c === 'i' || $c === 'o' || $c === 'u';
    }
    function trimTrailingVowels($s) {
        $i = strlen($s) - 1;
        while ($i >= 0 && $this->isVowel($s[$i])) $i--;
        return substr($s, 0, $i + 1);
    }
}
