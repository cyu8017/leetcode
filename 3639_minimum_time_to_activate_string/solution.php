<?php
// LeetCode 3639 - Minimum Time to Activate String
// https://leetcode.com/problems/minimum-time-to-activate-string/

class Solution {
    function minTime($s, $order, $k) {
        $n = strlen($s);
        $total = intdiv($n * ($n + 1), 2);
        if ($k > $total) return -1;
        $countValid = function($t) use ($n, $order, $total) {
            $star = array_fill(0, $n, false);
            for ($i = 0; $i <= $t; $i++) $star[$order[$i]] = true;
            $invalid = 0;
            for ($i = 0; $i < $n; ) {
                if ($star[$i]) { $i++; continue; }
                $j = $i;
                while ($j < $n && !$star[$j]) $j++;
                $L = $j - $i;
                $invalid += intdiv($L * ($L + 1), 2);
                $i = $j;
            }
            return $total - $invalid;
        };
        $lo = 0;
        $hi = $n - 1;
        $ans = -1;
        while ($lo <= $hi) {
            $mid = ($lo + $hi) >> 1;
            if ($countValid($mid) >= $k) {
                $ans = $mid;
                $hi = $mid - 1;
            } else $lo = $mid + 1;
        }
        return $ans;
    }
}
