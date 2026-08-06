<?php
// LeetCode 1137 - N-th Tribonacci Number
// https://leetcode.com/problems/n-th-tribonacci-number/

class Solution {
    /**
     * @param Integer $n
     * @return Integer
     */
    function tribonacci($n) {
        if ($n === 0) return 0;
        if ($n <= 2) return 1;
        $a = 0; $b = 1; $c = 1;
        for ($i = 3; $i <= $n; $i++) {
            $d = $a + $b + $c;
            $a = $b; $b = $c; $c = $d;
        }
        return $c;
    }
}
