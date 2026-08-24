<?php
// LeetCode 3227 - Vowels Game in a String
// https://leetcode.com/problems/vowels-game-in-a-string/

class Solution {
    function doesAliceWin($s) {
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $c = $s[$i];
            if ($c === 'a' || $c === 'e' || $c === 'i' || $c === 'o' || $c === 'u') return true;
        }
        return false;
    }
}
