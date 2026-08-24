<?php
// LeetCode 2828 - Check if a String Is an Acronym of Words
// https://leetcode.com/problems/check-if-a-string-is-an-acronym-of-words/

class Solution {
    function isAcronym($words, $s) {
        if (count($words) !== strlen($s)) return false;
        for ($i = 0; $i < count($words); $i++) {
            $w = $words[$i];
            if ($w === '' || $w[0] !== $s[$i]) return false;
        }
        return true;
    }
}
