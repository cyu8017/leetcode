<?php
// LeetCode 1646 - Get Maximum in Generated Array
// https://leetcode.com/problems/get-maximum-in-generated-array/

class Solution {
    /**
     * @param Integer $n
     * @return Integer
     */
    function getMaximumGenerated($n) {
        if ($n < 2) {
            return $n;
        }
        $a = array_fill(0, $n + 1, 0);
        $a[1] = 1;
        for ($i = 2; $i <= $n; $i++) {
            $a[$i] = $i % 2 === 0 ? $a[intdiv($i, 2)] : $a[intdiv($i, 2)] + $a[intdiv($i, 2) + 1];
        }
        return max($a);
    }
}
