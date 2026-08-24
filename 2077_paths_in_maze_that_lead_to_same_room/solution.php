<?php
// LeetCode 2077 - Paths in Maze That Lead to Same Room
// https://leetcode.com/problems/paths-in-maze-that-lead-to-same-room/

class Solution {
    /**
     * @param Integer $n
     * @param Integer[][] $corridors
     * @return Integer
     */
    function numberOfPaths($n, $corridors) {
        $g = array_fill(0, $n + 1, []);
        foreach ($corridors as $e) {
            $g[$e[0]][$e[1]] = true;
            $g[$e[1]][$e[0]] = true;
        }
        $ans = 0;
        foreach ($corridors as $e) {
            $a = $e[0];
            $b = $e[1];
            foreach ($g[$a] as $c => $_) if (isset($g[$b][$c])) $ans++;
        }
        return intdiv($ans, 3);
    }
}
