<?php
// LeetCode 2582 - Pass the Pillow
// https://leetcode.com/problems/pass-the-pillow/

class Solution {
    function passThePillow($n, $time) {
        $cycle = 2 * ($n - 1);
        $t = $time % $cycle;
        if ($t < $n) return 1 + $t;
        return $n - ($t - ($n - 1));
    }
}
