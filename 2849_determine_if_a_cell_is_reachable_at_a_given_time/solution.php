<?php
// LeetCode 2849 - Determine if a Cell Is Reachable at a Given Time
// https://leetcode.com/problems/determine-if-a-cell-is-reachable-at-a-given-time/

class Solution {
    function isReachableAtTime($sx, $sy, $fx, $fy, $t) {
        $need = max(abs($sx - $fx), abs($sy - $fy));
        if ($need === 0) return $t !== 1;
        return $t >= $need;
    }
}
