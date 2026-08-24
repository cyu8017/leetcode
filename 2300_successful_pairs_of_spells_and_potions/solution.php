<?php
// LeetCode 2300 - Successful Pairs of Spells and Potions
// https://leetcode.com/problems/successful-pairs-of-spells-and-potions/

class Solution {
    function successfulPairs($spells, $potions, $success) {
        sort($potions);
        $m = count($potions);
        $ans = array_fill(0, count($spells), 0);
        for ($i = 0; $i < count($spells); $i++) {
            $lo = 0;
            $hi = $m;
            while ($lo < $hi) {
                $mid = ($lo + $hi) >> 1;
                if ($spells[$i] * $potions[$mid] >= $success) $hi = $mid;
                else $lo = $mid + 1;
            }
            $ans[$i] = $m - $lo;
        }
        return $ans;
    }
}
