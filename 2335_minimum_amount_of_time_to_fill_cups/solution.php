<?php
// LeetCode 2335 - Minimum Amount of Time to Fill Cups
// https://leetcode.com/problems/minimum-amount-of-time-to-fill-cups/

class Solution {
    function fillCups($amount) {
        $a = $amount[0];
        $b = $amount[1];
        $c = $amount[2];
        if ($a < $b) { $t = $a; $a = $b; $b = $t; }
        if ($a < $c) { $t = $a; $a = $c; $c = $t; }
        if ($b < $c) { $t = $b; $b = $c; $c = $t; }
        if ($a >= $b + $c) return $a;
        return intdiv($a + $b + $c + 1, 2);
    }
}
