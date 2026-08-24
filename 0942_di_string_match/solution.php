<?php
// LeetCode 0942 - DI String Match
// https://leetcode.com/problems/di-string-match/

class Solution {
    function diStringMatch($s) {
        $lo = 0;
        $hi = strlen($s);
        $ans = array_fill(0, strlen($s) + 1, 0);
        $k = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            if ($s[$i] === "I") $ans[$k++] = $lo++;
            else $ans[$k++] = $hi--;
        }
        $ans[$k] = $lo;
        return $ans;
    }
}
