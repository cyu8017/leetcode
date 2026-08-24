<?php
// LeetCode 3226 - Number of Bit Changes to Make Two Integers Equal
// https://leetcode.com/problems/number-of-bit-changes-to-make-two-integers-equal/

class Solution {
    function minChanges($n, $k) {
        if (($n & $k) !== $k) return -1;
        $x = $n ^ $k;
        $c = 0;
        while ($x) { $c += $x & 1; $x >>= 1; }
        return $c;
    }
}
