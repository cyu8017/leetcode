<?php
// LeetCode 2731 - Movement of Robots
// https://leetcode.com/problems/movement-of-robots/

class Solution {
    function sumDistance($nums, $s, $d) {
        $MOD = 1000000007;
        $n = count($nums);
        $pos = [];
        for ($i = 0; $i < $n; $i++) $pos[$i] = $nums[$i] + ($s[$i] === 'R' ? $d : -$d);
        sort($pos);
        $ans = 0;
        $pref = 0;
        for ($i = 0; $i < $n; $i++) {
            $ans = ($ans + (($pos[$i] * $i - $pref) % $MOD + $MOD) % $MOD) % $MOD;
            $pref += $pos[$i];
        }
        return ($ans % $MOD + $MOD) % $MOD;
    }
}
