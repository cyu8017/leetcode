<?php
// LeetCode 0780 - Reaching Points
// https://leetcode.com/problems/reaching-points/

class Solution {
    /**
     * @param Integer $sx
     * @param Integer $sy
     * @param Integer $tx
     * @param Integer $ty
     * @return Boolean
     */
    function reachingPoints($sx, $sy, $tx, $ty) {
        while ($tx >= $sx && $ty >= $sy) {
            if ($tx === $sx && $ty === $sy) return true;
            if ($tx === $ty) break;
            if ($tx > $ty) {
                if ($ty > $sy) $tx %= $ty;
                else return ($tx - $sx) % $ty === 0;
            } else {
                if ($tx > $sx) $ty %= $tx;
                else return ($ty - $sy) % $tx === 0;
            }
        }
        return $tx === $sx && $ty === $sy;
    }
}
