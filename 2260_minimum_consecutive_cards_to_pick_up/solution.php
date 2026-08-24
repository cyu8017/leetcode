<?php
// LeetCode 2260 - Minimum Consecutive Cards to Pick Up
// https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up/

class Solution {
    function minimumCardPickup($cards) {
        $last = [];
        $ans = -1;
        for ($i = 0; $i < count($cards); $i++) {
            if (isset($last[$cards[$i]])) {
                $diff = $i - $last[$cards[$i]] + 1;
                if ($ans === -1 || $diff < $ans) $ans = $diff;
            }
            $last[$cards[$i]] = $i;
        }
        return $ans;
    }
}
