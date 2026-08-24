<?php
// LeetCode 0755 - Pour Water
// https://leetcode.com/problems/pour-water/

class Solution {
    function pourWater($heights, $volume, $k) {
        for ($v = 0; $v < $volume; $v++) {
            $index = $k;
            for ($i = $k - 1; $i >= 0; $i--) {
                if ($heights[$i] > $heights[$index]) break;
                if ($heights[$i] < $heights[$index]) $index = $i;
            }
            if ($index !== $k) { $heights[$index]++; continue; }
            $index = $k;
            for ($i = $k + 1; $i < count($heights); $i++) {
                if ($heights[$i] > $heights[$index]) break;
                if ($heights[$i] < $heights[$index]) $index = $i;
            }
            $heights[$index]++;
        }
        return $heights;
    }
}
