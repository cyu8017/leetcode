<?php
// LeetCode 3670 - Maximum Product of Two Integers With No Common Bits
// https://leetcode.com/problems/maximum-product-of-two-integers-with-no-common-bits/

class Solution {
    function maxProduct($nums) {
        $maxV = 0;
        foreach ($nums as $v) if ($v > $maxV) $maxV = $v;
        $bitsN = 0;
        for ($x = $maxV; $x > 0; $x >>= 1) $bitsN++;
        if ($bitsN === 0) $bitsN = 1;
        $size = 1 << $bitsN;
        $best = array_fill(0, $size, 0);
        foreach ($nums as $v) if ($v > $best[$v]) $best[$v] = $v;
        for ($mask = 0; $mask < $size; $mask++) {
            for ($b = 0; $b < $bitsN; $b++) {
                if (($mask & (1 << $b)) !== 0) {
                    $sub = $mask ^ (1 << $b);
                    if ($best[$sub] > $best[$mask]) $best[$mask] = $best[$sub];
                }
            }
        }
        $ans = 0;
        foreach ($nums as $v) {
            $comp = ($size - 1) ^ $v;
            if ($best[$comp] > 0) {
                $p = $v * $best[$comp];
                if ($p > $ans) $ans = $p;
            }
        }
        return $ans;
    }
}
