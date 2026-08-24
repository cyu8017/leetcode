<?php
// LeetCode 3524 - Find X Value of Array I
// https://leetcode.com/problems/find-x-value-of-array-i/

class Solution {
    function resultArray($nums, $k) {
        $ans = array_fill(0, $k, 0);
        $dp = array_fill(0, $k, 0);
        foreach ($nums as $num) {
            $newDp = array_fill(0, $k, 0);
            $nm = $num % $k;
            $newDp[$nm] = 1;
            for ($i = 0; $i < $k; $i++) $newDp[($i * $nm) % $k] += $dp[$i];
            for ($i = 0; $i < $k; $i++) $ans[$i] += $newDp[$i];
            $dp = $newDp;
        }
        return $ans;
    }
}
