<?php
// LeetCode 3599 - Partition Array to Minimize XOR
// https://leetcode.com/problems/partition-array-to-minimize-xor/

class Solution {
    function minXor($nums, $k) {
        $n = count($nums);
        $g = array_fill(0, $n + 1, 0);
        for ($i = 1; $i <= $n; $i++) $g[$i] = $g[$i - 1] ^ $nums[$i - 1];
        $Inf = intdiv(2147483647, 2);
        $f = [];
        for ($i = 0; $i <= $n; $i++) $f[$i] = array_fill(0, $k + 1, $Inf);
        $f[0][0] = 0;
        for ($i = 1; $i <= $n; $i++) {
            for ($j = 1; $j <= min($i, $k); $j++) {
                for ($h = $j - 1; $h < $i; $h++) {
                    $f[$i][$j] = min($f[$i][$j], max($f[$h][$j - 1], $g[$i] ^ $g[$h]));
                }
            }
        }
        return $f[$n][$k];
    }
}
