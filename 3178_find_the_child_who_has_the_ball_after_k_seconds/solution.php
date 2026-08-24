<?php
// LeetCode 3178 - Find the Child Who Has the Ball After K Seconds
// https://leetcode.com/problems/find-the-child-who-has-the-ball-after-k-seconds/

class Solution {
    function numberOfChild($n, $k) {
        $mod = $k % ($n - 1);
        $k = intdiv($k, $n - 1);
        if ($k % 2 === 1) return $n - $mod - 1;
        return $mod;
    }
}
