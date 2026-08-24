<?php
// LeetCode 2390 - Removing Stars From a String
// https://leetcode.com/problems/removing-stars-from-a-string/

class Solution {
    function removeStars($s) {
        $stack = [];
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            if ($s[$i] === '*') array_pop($stack);
            else $stack[] = $s[$i];
        }
        return implode('', $stack);
    }
}
