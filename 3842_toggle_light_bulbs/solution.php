<?php
// LeetCode 3842 - Toggle Light Bulbs
// https://leetcode.com/problems/toggle-light-bulbs/

class Solution {
    function toggleLightBulbs($bulbs) {
        $st = array_fill(0, 101, 0);
        foreach ($bulbs as $x) $st[$x] ^= 1;
        $ans = [];
        for ($i = 0; $i < 101; $i++) if ($st[$i] === 1) $ans[] = $i;
        return $ans;
    }
}
