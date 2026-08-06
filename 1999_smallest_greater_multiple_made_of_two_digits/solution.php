<?php
// LeetCode 1999 - Smallest Greater Multiple Made of Two Digits
// https://leetcode.com/problems/smallest-greater-multiple-made-of-two-digits/

class Solution {
    /**
     * @param Integer $k
     * @param Integer $digit1
     * @param Integer $digit2
     * @return Integer
     */
    function findInteger($k, $digit1, $digit2) {
        $digits = array_values(array_unique([$digit1, $digit2]));
        sort($digits);
        $q = [];
        $seen = [];
        foreach ($digits as $d) {
            if ($d !== 0) {
                $q[] = $d;
                $seen[$d] = true;
            }
        }
        if (!$q) {
            return -1;
        }
        $maxInt = 2147483647;
        $qi = 0;
        while ($qi < count($q)) {
            $x = $q[$qi++];
            if ($x > $k && $x % $k === 0) {
                return $x;
            }
            foreach ($digits as $d) {
                $nx = $x * 10 + $d;
                if ($nx <= $maxInt && !isset($seen[$nx])) {
                    $seen[$nx] = true;
                    $q[] = $nx;
                }
            }
        }
        return -1;
    }
}
