<?php
// LeetCode 1745 - Palindrome Partitioning IV
// https://leetcode.com/problems/palindrome-partitioning-iv/

class Solution {
    /**
     * @param String $s
     * @return Boolean
     */
    function checkPartitioning($s) {
        $n = strlen($s);
        $pal = array_fill(0, $n, array_fill(0, $n, false));
        for ($i = $n - 1; $i >= 0; $i--) {
            for ($j = $i; $j < $n; $j++) {
                $pal[$i][$j] = $s[$i] === $s[$j] && ($j - $i < 2 || $pal[$i + 1][$j - 1]);
            }
        }
        for ($i = 0; $i < $n - 2; $i++) {
            for ($j = $i + 1; $j < $n - 1; $j++) {
                if ($pal[0][$i] && $pal[$i + 1][$j] && $pal[$j + 1][$n - 1]) {
                    return true;
                }
            }
        }
        return false;
    }
}
