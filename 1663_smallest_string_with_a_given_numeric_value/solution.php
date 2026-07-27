<?php
// LeetCode 1663 - Smallest String With A Given Numeric Value
// https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/

class Solution {
    function getSmallestString($n, $k) {
        $a = array_fill(0, $n, "a");
        $k -= $n;
        for ($i = $n - 1; $i >= 0; $i--) {
            $d = min(25, $k);
            $a[$i] = chr(97 + $d);
            $k -= $d;
        }
        return implode("", $a);
    }
}
