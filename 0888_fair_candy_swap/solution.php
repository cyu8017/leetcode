<?php
// LeetCode 0888 - Fair Candy Swap
// https://leetcode.com/problems/fair-candy-swap/

class Solution {
    function fairCandySwap($aliceSizes, $bobSizes) {
        $sumA = array_sum($aliceSizes);
        $sumB = array_sum($bobSizes);
        $diff = intdiv($sumA - $sumB, 2);
        $bob = array_flip($bobSizes);
        foreach ($aliceSizes as $a) {
            $need = $a - $diff;
            if (array_key_exists($need, $bob)) return [$a, $need];
        }
        return [];
    }
}
