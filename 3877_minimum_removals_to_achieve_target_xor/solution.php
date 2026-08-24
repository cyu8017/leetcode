<?php
// LeetCode 3877 - Minimum Removals to Achieve Target XOR
// https://leetcode.com/problems/minimum-removals-to-achieve-target-xor/

class Solution {
    function minRemovals($nums, $target) {
        $mx = 0;
        foreach ($nums as $x) $mx = max($mx, $x);
        $m = 0;
        if ($mx > 0) {
            $u = $mx;
            while ($u !== 0) { $m++; $u >>= 1; }
        }
        if ((1 << $m) <= $target) return -1;
        $n = count($nums);
        $N = 1 << $m;
        $NEG = PHP_INT_MIN / 4;
        $f = [];
        for ($i = 0; $i <= $n; $i++) $f[$i] = array_fill(0, $N, $NEG);
        $f[0][0] = 0;
        for ($i = 1; $i <= $n; $i++) {
            $x = $nums[$i - 1];
            for ($j = 0; $j < $N; $j++) {
                $f[$i][$j] = $f[$i - 1][$j];
                if ($f[$i - 1][$j ^ $x] !== $NEG) {
                    $f[$i][$j] = max($f[$i][$j], $f[$i - 1][$j ^ $x] + 1);
                }
            }
        }
        if ($f[$n][$target] < 0) return -1;
        return $n - $f[$n][$target];
    }
}
