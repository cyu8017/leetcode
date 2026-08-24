<?php
// LeetCode 2350 - Shortest Impossible Sequence of Rolls
// https://leetcode.com/problems/shortest-impossible-sequence-of-rolls/

class Solution {
    function shortestSequence($rolls, $k) {
        $seen = [];
        $ans = 1;
        foreach ($rolls as $r) {
            $seen[$r] = true;
            if (count($seen) === $k) {
                $ans++;
                $seen = [];
            }
        }
        return $ans;
    }
}
