<?php
// LeetCode 3407 - Substring Matching Pattern
// https://leetcode.com/problems/substring-matching-pattern/

class Solution {
    function hasMatch($s, $p) {
        $i = strpos($p, '*');
        $left = substr($p, 0, $i);
        $right = substr($p, $i + 1);
        $li = $left === '' ? 0 : strpos($s, $left);
        if ($li === false) return false;
        $from = $li + strlen($left);
        if ($right === '') return true;
        return strpos($s, $right, $from) !== false;
    }
}
