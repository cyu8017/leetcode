<?php
// LeetCode 3412 - Find Mirror Score of a String
// https://leetcode.com/problems/find-mirror-score-of-a-string/

class Solution {
    function calculateScore($s) {
        $stacks = [];
        for ($i = 0; $i < 26; $i++) $stacks[$i] = [];
        $ans = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $ci = ord($s[$i]) - 97;
            $mir = 25 - $ci;
            if (count($stacks[$mir])) {
                $j = array_pop($stacks[$mir]);
                $ans += $i - $j;
            } else {
                $stacks[$ci][] = $i;
            }
        }
        return $ans;
    }
}
