<?php
// LeetCode 1054 - Distant Barcodes
// https://leetcode.com/problems/distant-barcodes/

class Solution {
    /**
     * @param Integer[] $barcodes
     * @return Integer[]
     */
    function rearrangeBarcodes($barcodes) {
        $count = [];
        foreach ($barcodes as $v) {
            $count[$v] = ($count[$v] ?? 0) + 1;
        }
        $pairs = [];
        foreach ($count as $value => $freq) {
            $pairs[] = [$value, $freq];
        }
        usort($pairs, function ($a, $b) {
            if ($a[1] !== $b[1]) {
                return $b[1] <=> $a[1];
            }
            return $b[0] <=> $a[0];
        });
        $n = count($barcodes);
        $ans = array_fill(0, $n, 0);
        $i = 0;
        foreach ($pairs as [$value, $freq]) {
            for ($k = 0; $k < $freq; $k++) {
                $ans[$i] = $value;
                $i += 2;
                if ($i >= $n) {
                    $i = 1;
                }
            }
        }
        return $ans;
    }
}
