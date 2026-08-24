<?php
// LeetCode 0821 - Shortest Distance to a Character
// https://leetcode.com/problems/shortest-distance-to-a-character/

class Solution {
    /**
     * @param String $s
     * @param String $c
     * @return Integer[]
     */
    function shortestToChar($s, $c) {
        $n = strlen($s);
        $ans = array_fill(0, $n, 0);
        $prev = -$n;
        for ($i = 0; $i < $n; $i++) {
            if ($s[$i] === $c) $prev = $i;
            $ans[$i] = $i - $prev;
        }
        $prev = 2 * $n;
        for ($i = $n - 1; $i >= 0; $i--) {
            if ($s[$i] === $c) $prev = $i;
            $ans[$i] = min($ans[$i], $prev - $i);
        }
        return $ans;
    }
}
