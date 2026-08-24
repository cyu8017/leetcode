<?php
// LeetCode 2682 - Find the Losers of the Circular Game
// https://leetcode.com/problems/find-the-losers-of-the-circular-game/

class Solution {
    function circularGameLosers($n, $k) {
        $seen = array_fill(0, $n + 1, false);
        $cur = 1;
        $step = 1;
        while (!$seen[$cur]) {
            $seen[$cur] = true;
            $cur = ($cur - 1 + $step * $k) % $n + 1;
            $step++;
        }
        $ans = [];
        for ($i = 1; $i <= $n; $i++) if (!$seen[$i]) $ans[] = $i;
        return $ans;
    }
}
