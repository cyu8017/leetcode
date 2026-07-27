<?php
// LeetCode 1675 - Minimize Deviation in Array
// https://leetcode.com/problems/minimize-deviation-in-array/

class Solution {
    function minimumDeviation($nums) {
        $h = new SplMaxHeap();
        $mn = PHP_INT_MAX;
        foreach ($nums as $x) {
            if ($x % 2) $x *= 2;
            $mn = min($mn, $x);
            $h->insert($x);
        }
        $ans = PHP_INT_MAX;
        while (true) {
            $x = $h->extract();
            $ans = min($ans, $x - $mn);
            if ($x % 2) return $ans;
            $x = intdiv($x, 2);
            $mn = min($mn, $x);
            $h->insert($x);
        }
    }
}
