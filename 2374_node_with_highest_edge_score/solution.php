<?php
// LeetCode 2374 - Node With Highest Edge Score
// https://leetcode.com/problems/node-with-highest-edge-score/

class Solution {
    function edgeScore($edges) {
        $n = count($edges);
        $score = array_fill(0, $n, 0);
        for ($i = 0; $i < $n; $i++) $score[$edges[$i]] += $i;
        $ans = 0;
        for ($i = 1; $i < $n; $i++)
            if ($score[$i] > $score[$ans]) $ans = $i;
        return $ans;
    }
}
