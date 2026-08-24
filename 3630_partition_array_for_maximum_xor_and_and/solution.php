<?php
// LeetCode 3630 - Partition Array for Maximum XOR and AND
// https://leetcode.com/problems/partition-array-for-maximum-xor-and-and/

class Solution {
    function maximizeXorAndXor($nums) {
        $n = count($nums);
        $best = 0;
        for ($mask = 0; $mask < (1 << $n); $mask++) {
            $andVal = -1;
            $xorRest = 0;
            for ($i = 0; $i < $n; $i++) {
                if ((($mask >> $i) & 1) !== 0) {
                    $andVal = $andVal < 0 ? $nums[$i] : ($andVal & $nums[$i]);
                } else {
                    $xorRest ^= $nums[$i];
                }
            }
            if ($andVal < 0) $andVal = 0;
            $comp = ((1 << $n) - 1) ^ $mask;
            for ($sub = $comp; ; $sub = ($sub - 1) & $comp) {
                $x1 = 0;
                for ($i = 0; $i < $n; $i++)
                    if ((($sub >> $i) & 1) !== 0) $x1 ^= $nums[$i];
                $x2 = $xorRest ^ $x1;
                $best = max($best, $andVal + $x1 + $x2);
                if ($sub === 0) break;
            }
        }
        return $best;
    }
}
