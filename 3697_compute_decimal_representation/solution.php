<?php
// LeetCode 3697 - Compute Decimal Representation
// https://leetcode.com/problems/compute-decimal-representation/

class Solution {
    function decimalRepresentation($n) {
        $ans = [];
        $p = 1;
        while ($n > 0) {
            $v = $n % 10;
            $n = intdiv($n, 10);
            if ($v !== 0) $ans[] = $p * $v;
            $p *= 10;
        }
        return array_reverse($ans);
    }
}
