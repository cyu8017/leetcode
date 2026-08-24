<?php
// LeetCode 3009 - Maximum Number of Intersections on the Chart
// https://leetcode.com/problems/maximum-number-of-intersections-on-the-chart/

class Solution {
    function maxIntersectionCount($y) {
        $n = count($y);
        $line = [];
        for ($i = 1; $i < $n; $i++) {
            $start = 2 * $y[$i - 1];
            $end = 2 * $y[$i];
            if ($i !== $n - 1) {
                if ($y[$i] > $y[$i - 1]) $end--;
                else $end++;
            }
            $a = $start;
            $b = $end;
            if ($a > $b) { $t = $a; $a = $b; $b = $t; }
            $line[$a] = ($line[$a] ?? 0) + 1;
            $line[$b + 1] = ($line[$b + 1] ?? 0) - 1;
        }
        $keys = array_keys($line);
        sort($keys);
        $ans = 0;
        $cur = 0;
        foreach ($keys as $key) {
            $cur += $line[$key];
            if ($cur > $ans) $ans = $cur;
        }
        return $ans;
    }
}
