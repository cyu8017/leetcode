<?php
// LeetCode 3443 - Maximum Manhattan Distance After K Changes
// https://leetcode.com/problems/maximum-manhattan-distance-after-k-changes/

class Solution {
    function maxDistance($s, $k) {
        $ans = 0;
        $lat = 0;
        $lon = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $c = $s[$i];
            if ($c === "N") $lat++;
            else if ($c === "S") $lat--;
            else if ($c === "E") $lon++;
            else $lon--;
            $md = abs($lat) + abs($lon);
            $steps = $i + 1;
            $cur = $md + 2 * $k;
            if ($cur > $steps) $cur = $steps;
            if ($cur > $ans) $ans = $cur;
        }
        return $ans;
    }
}
