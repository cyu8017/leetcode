<?php
// LeetCode 1652 - Defuse the Bomb
// https://leetcode.com/problems/defuse-the-bomb/

class Solution {
    function decrypt($code, $k) {
        $n = count($code);
        if ($k === 0) return array_fill(0, $n, 0);
        $a = array_merge($code, $code);
        $ans = [];
        for ($i = 0; $i < $n; $i++) {
            if ($k > 0) {
                $ans[] = array_sum(array_slice($a, $i + 1, $k));
            } else {
                $ans[] = array_sum(array_slice($a, $i + $n + $k, -$k));
            }
        }
        return $ans;
    }
}
