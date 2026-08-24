<?php
// LeetCode 2064 - Minimized Maximum of Products Distributed to Any Store
// https://leetcode.com/problems/minimized-maximum-of-products-distributed-to-any-store/

class Solution {
    /**
     * @param Integer $n
     * @param Integer[] $quantities
     * @return Integer
     */
    function minimizedMaximum($n, $quantities) {
        $can = function ($x) use ($quantities, $n) {
            $need = 0;
            foreach ($quantities as $q) {
                $need += intdiv($q + $x - 1, $x);
                if ($need > $n) return false;
            }
            return true;
        };
        $lo = 1;
        $hi = 0;
        foreach ($quantities as $q) $hi = max($hi, $q);
        while ($lo < $hi) {
            $mid = ($lo + $hi) >> 1;
            if ($can($mid)) $hi = $mid;
            else $lo = $mid + 1;
        }
        return $lo;
    }
}
