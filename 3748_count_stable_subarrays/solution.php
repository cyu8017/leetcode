<?php
// LeetCode 3748 - Count Stable Subarrays
// https://leetcode.com/problems/count-stable-subarrays/

class Solution {
    function countStableSubarrays($nums, $queries) {
        $n = count($nums);
        $seg = [];
        $s = [0];
        $l = 0;
        for ($r = 0; $r < $n; $r++) {
            if ($r === $n - 1 || $nums[$r] > $nums[$r + 1]) {
                $seg[] = $l;
                $k = $r - $l + 1;
                $s[] = $s[count($s) - 1] + $k * ($k + 1) / 2;
                $l = $r + 1;
            }
        }
        $lowerBound = function($a, $x) {
            $lo = 0;
            $hi = count($a);
            while ($lo < $hi) {
                $mid = ($lo + $hi) >> 1;
                if ($a[$mid] < $x) $lo = $mid + 1;
                else $hi = $mid;
            }
            return $lo;
        };
        $ans = array_fill(0, count($queries), 0);
        for ($idx = 0; $idx < count($queries); $idx++) {
            $left = $queries[$idx][0];
            $right = $queries[$idx][1];
            $i = $lowerBound($seg, $left + 1);
            $j = $lowerBound($seg, $right + 1) - 1;
            if ($i > $j) {
                $k = $right - $left + 1;
                $ans[$idx] = $k * ($k + 1) / 2;
            } else {
                $a = $seg[$i] - $left;
                $b = $right - $seg[$j] + 1;
                $ans[$idx] = $a * ($a + 1) / 2 + $s[$j] - $s[$i] + $b * ($b + 1) / 2;
            }
        }
        return $ans;
    }
}
