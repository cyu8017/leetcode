<?php
// LeetCode 3672 - Sum of Weighted Modes in Subarrays
// https://leetcode.com/problems/sum-of-weighted-modes-in-subarrays/

class Solution {
    function modeWeight($nums, $k) {
        $cnt = [];
        $pq = [];
        $push = function($freq, $val) use (&$pq) {
            $pq[] = [$freq, $val];
            usort($pq, function($a, $b) {
                if ($a[0] !== $b[0]) return $b[0] <=> $a[0];
                return $a[1] <=> $b[1];
            });
        };
        $getMode = function() use (&$pq, &$cnt) {
            while (true) {
                $top = $pq[0];
                $freq = $top[0];
                $val = $top[1];
                if ((isset($cnt[$val]) ? $cnt[$val] : 0) === $freq) return $freq * $val;
                array_shift($pq);
            }
        };
        for ($i = 0; $i < $k; $i++) {
            $x = $nums[$i];
            if (!isset($cnt[$x])) $cnt[$x] = 0;
            $cnt[$x]++;
            $push($cnt[$x], $x);
        }
        $ans = $getMode();
        $n = count($nums);
        for ($i = $k; $i < $n; $i++) {
            $x = $nums[$i];
            $y = $nums[$i - $k];
            if (!isset($cnt[$x])) $cnt[$x] = 0;
            $cnt[$x]++;
            $cnt[$y]--;
            $push($cnt[$x], $x);
            $push($cnt[$y], $y);
            $ans += $getMode();
        }
        return $ans;
    }
}
