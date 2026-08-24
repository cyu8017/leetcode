<?php
// LeetCode 3532 - Path Existence Queries in a Graph I
// https://leetcode.com/problems/path-existence-queries-in-a-graph-i/

class Solution {
    function pathExistenceQueries($n, $nums, $maxDiff, $queries) {
        $g = array_fill(0, $n, 0);
        $cnt = 0;
        for ($i = 1; $i < $n; $i++) {
            if ($nums[$i] - $nums[$i - 1] > $maxDiff) $cnt++;
            $g[$i] = $cnt;
        }
        $ans = array_fill(0, count($queries), false);
        for ($i = 0; $i < count($queries); $i++)
            $ans[$i] = $g[$queries[$i][0]] === $g[$queries[$i][1]];
        return $ans;
    }
}
