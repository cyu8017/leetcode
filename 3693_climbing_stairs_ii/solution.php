<?php
// LeetCode 3693 - Climbing Stairs II
// https://leetcode.com/problems/climbing-stairs-ii/

class Solution {
    function climbStairs($n, $costs) {
        $inf = 1000000000;
        $f = array_fill(0, $n + 1, $inf);
        $f[0] = 0;
        for ($i = 1; $i <= $n; $i++) {
            $x = $costs[$i - 1];
            for ($j = max(0, $i - 3); $j < $i; $j++) {
                $f[$i] = min($f[$i], $f[$j] + $x + ($i - $j) * ($i - $j));
            }
        }
        return $f[$n];
    }
}
