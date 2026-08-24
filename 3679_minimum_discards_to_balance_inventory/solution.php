<?php
// LeetCode 3679 - Minimum Discards to Balance Inventory
// https://leetcode.com/problems/minimum-discards-to-balance-inventory/

class Solution {
    function minArrivalsToDiscard($arrivals, $w, $m) {
        $cnt = [];
        $n = count($arrivals);
        $marked = array_fill(0, $n, 0);
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            $x = $arrivals[$i];
            if ($i >= $w) {
                if (!isset($cnt[$arrivals[$i - $w]])) $cnt[$arrivals[$i - $w]] = 0;
                $cnt[$arrivals[$i - $w]] -= $marked[$i - $w];
            }
            if ((isset($cnt[$x]) ? $cnt[$x] : 0) >= $m) $ans++;
            else {
                $marked[$i] = 1;
                if (!isset($cnt[$x])) $cnt[$x] = 0;
                $cnt[$x]++;
            }
        }
        return $ans;
    }
}
