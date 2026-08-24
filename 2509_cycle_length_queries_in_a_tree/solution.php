<?php
// LeetCode 2509 - Cycle Length Queries in a Tree
// https://leetcode.com/problems/cycle-length-queries-in-a-tree/

class Solution {
    function cycleLengthQueries($n, $queries) {
        $ans = array_fill(0, count($queries), 0);
        for ($i = 0; $i < count($queries); $i++) {
            $a = $queries[$i][0];
            $b = $queries[$i][1];
            $steps = 0;
            while ($a !== $b) {
                if ($a > $b) $a = intdiv($a, 2);
                else $b = intdiv($b, 2);
                $steps++;
            }
            $ans[$i] = $steps + 1;
        }
        return $ans;
    }
}
