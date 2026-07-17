<?php
// LeetCode 1738 - Find Kth Largest XOR Coordinate Value
// https://leetcode.com/problems/find-kth-largest-xor-coordinate-value/

class Solution {
    /**
     * @param Integer[][] $matrix
     * @param Integer $k
     * @return Integer
     */
    function kthLargestValue($matrix, $k) {
        $rows = count($matrix);
        $cols = count($matrix[0]);
        $pref = array_fill(0, $rows + 1, array_fill(0, $cols + 1, 0));
        $values = [];
        for ($r = 1; $r <= $rows; $r++) {
            for ($c = 1; $c <= $cols; $c++) {
                $pref[$r][$c] = $pref[$r - 1][$c] ^ $pref[$r][$c - 1] ^ $pref[$r - 1][$c - 1] ^ $matrix[$r - 1][$c - 1];
                $values[] = $pref[$r][$c];
            }
        }
        rsort($values);
        return $values[$k - 1];
    }
}
