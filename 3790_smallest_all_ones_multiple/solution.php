<?php
// LeetCode 3790 - Smallest All-Ones Multiple
// https://leetcode.com/problems/smallest-all-ones-multiple/

class Solution {
    function minAllOneMultiple($k) {
        if (($k & 1) === 0) return -1;
        $x = 1 % $k;
        $ans = 1;
        for ($i = 0; $i < $k; $i++) {
            $x = ($x * 10 + 1) % $k;
            $ans++;
            if ($x === 0) return $ans;
        }
        return -1;
    }
}
