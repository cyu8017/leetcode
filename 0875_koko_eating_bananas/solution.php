<?php
// LeetCode 0875 - Koko Eating Bananas
// https://leetcode.com/problems/koko-eating-bananas/

class Solution {
    /**
     * @param Integer[] $piles
     * @param Integer $h
     * @return Integer
     */
    function minEatingSpeed($piles, $h) {
        $lo = 1;
        $hi = 0;
        foreach ($piles as $p) $hi = max($hi, $p);
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi, 2);
            $hours = 0;
            foreach ($piles as $p) $hours += intdiv($p + $mid - 1, $mid);
            if ($hours <= $h) $hi = $mid;
            else $lo = $mid + 1;
        }
        return $lo;
    }
}
