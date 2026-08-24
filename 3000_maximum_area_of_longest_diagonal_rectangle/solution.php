<?php
// LeetCode 3000 - Maximum Area of Longest Diagonal Rectangle
// https://leetcode.com/problems/maximum-area-of-longest-diagonal-rectangle/

class Solution {
    function areaOfMaxDiagonal($dimensions) {
        $ans = 0;
        $mx = 0;
        foreach ($dimensions as $d) {
            $l = $d[0];
            $w = $d[1];
            $t = $l * $l + $w * $w;
            if ($mx < $t) {
                $mx = $t;
                $ans = $l * $w;
            } else if ($mx === $t) {
                $ans = max($ans, $l * $w);
            }
        }
        return $ans;
    }
}
