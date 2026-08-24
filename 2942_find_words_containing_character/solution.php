<?php
// LeetCode 2942 - Find Words Containing Character
// https://leetcode.com/problems/find-words-containing-character/

class Solution {
    function findWordsContaining($words, $x) {
        $ans = [];
        for ($i = 0; $i < count($words); $i++) {
            if (strpos($words[$i], $x) !== false) $ans[] = $i;
        }
        return $ans;
    }
}
