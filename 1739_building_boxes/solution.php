<?php
// LeetCode 1739 - Building Boxes
// https://leetcode.com/problems/building-boxes/

class Solution {
    /**
     * @param Integer $n
     * @return Integer
     */
    function minimumBoxes($n) {
        $height = 0;
        $used = 0;
        $base = 0;
        while ($used + intdiv(($height + 1) * ($height + 2), 2) <= $n) {
            $height++;
            $layer = intdiv($height * ($height + 1), 2);
            $used += $layer;
            $base += $height;
        }
        $extra = 0;
        while ($used < $n) {
            $extra++;
            $used += $extra;
        }
        return $base + $extra;
    }
}
