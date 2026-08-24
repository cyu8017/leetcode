<?php
// LeetCode 3082 - Find the Sum of the Power of All Subsequences
// https://leetcode.com/problems/find-the-sum-of-the-power-of-all-subsequences/

class Solution {
    function sumOfPower($nums, $k) {
        $MOD = 1000000007;
        $n = count($nums);
        $f = [];
        for ($i = 0; $i <= $n; $i++) $f[] = array_fill(0, $k + 1, 0);
        $f[0][0] = 1;
        for ($i = 1; $i <= $n; $i++) {
            for ($j = 0; $j <= $k; $j++) {
                $f[$i][$j] = ($f[$i - 1][$j] * 2) % $MOD;
                if ($j >= $nums[$i - 1])
                    $f[$i][$j] = ($f[$i][$j] + $f[$i - 1][$j - $nums[$i - 1]]) % $MOD;
            }
        }
        return $f[$n][$k];
    }
}
