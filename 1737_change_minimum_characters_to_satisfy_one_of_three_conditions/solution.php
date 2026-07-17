<?php
// LeetCode 1737 - Change Minimum Characters to Satisfy One of Three Conditions
// https://leetcode.com/problems/change-minimum-characters-to-satisfy-one-of-three-conditions/

class Solution {
    /**
     * @param String $a
     * @param String $b
     * @return Integer
     */
    function minCharacters($a, $b) {
        $ca = array_fill(0, 26, 0);
        $cb = array_fill(0, 26, 0);
        $n = strlen($a);
        $m = strlen($b);
        for ($i = 0; $i < $n; $i++) {
            $ca[ord($a[$i]) - 97]++;
        }
        for ($i = 0; $i < $m; $i++) {
            $cb[ord($b[$i]) - 97]++;
        }
        $ans = $n + $m - max(max($ca), max($cb));
        $preA = 0;
        $preB = 0;
        for ($code = 0; $code < 25; $code++) {
            $preA += $ca[$code];
            $preB += $cb[$code];
            $ans = min($ans, $n - $preA + $preB, $m - $preB + $preA);
        }
        return $ans;
    }
}
