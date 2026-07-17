<?php
// LeetCode 1758 - Minimum Changes To Make Alternating Binary String
// https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/

class Solution {
    /**
     * @param String $s
     * @return Integer
     */
    function minOperations($s) {
        $alt1 = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $expected = ($i % 2 === 0) ? '0' : '1';
            if ($s[$i] !== $expected) {
                $alt1++;
            }
        }
        return min($alt1, $n - $alt1);
    }
}
