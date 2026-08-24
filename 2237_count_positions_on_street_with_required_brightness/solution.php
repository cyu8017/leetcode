<?php
// LeetCode 2237 - Count Positions on Street With Required Brightness
// https://leetcode.com/problems/count-positions-on-street-with-required-brightness/

class Solution {
    function solve($n, $lights, $requirement) {
        $diff = array_fill(0, $n + 1, 0);
        foreach ($lights as $light) {
            $pos = $light[0];
            $r = $light[1];
            $l = max(0, $pos - $r);
            $rr = min($n - 1, $pos + $r);
            $diff[$l]++;
            $diff[$rr + 1]--;
        }
        $ans = 0;
        $cur = 0;
        for ($i = 0; $i < $n; $i++) {
            $cur += $diff[$i];
            if ($cur >= $requirement[$i]) $ans++;
        }
        return $ans;
    }
}
