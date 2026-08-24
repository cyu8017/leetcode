<?php
// LeetCode 3200 - Maximum Height of a Triangle
// https://leetcode.com/problems/maximum-height-of-a-triangle/

class Solution {
    function maxHeightOfTriangle($red, $blue) {
        $ans = 0;
        for ($k = 0; $k < 2; $k++) {
            $c = [$red, $blue];
            for ($i = 1, $j = $k; $i <= $c[$j]; $i++, $j ^= 1) {
                $c[$j] -= $i;
                $ans = max($ans, $i);
            }
        }
        return $ans;
    }
}
