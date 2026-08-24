<?php
// LeetCode 0949 - Largest Time for Given Digits
// https://leetcode.com/problems/largest-time-for-given-digits/

class Solution {
    function largestTimeFromDigits($arr) {
        sort($arr);
        $best = "";
        $nextPermutation = function (&$a) {
            $i = count($a) - 2;
            while ($i >= 0 && $a[$i] >= $a[$i + 1]) $i--;
            if ($i < 0) return false;
            $j = count($a) - 1;
            while ($a[$j] <= $a[$i]) $j--;
            $tmp = $a[$i]; $a[$i] = $a[$j]; $a[$j] = $tmp;
            for ($l = $i + 1, $r = count($a) - 1; $l < $r; $l++, $r--) {
                $tmp = $a[$l]; $a[$l] = $a[$r]; $a[$r] = $tmp;
            }
            return true;
        };
        do {
            $hours = 10 * $arr[0] + $arr[1];
            $minutes = 10 * $arr[2] + $arr[3];
            if ($hours < 24 && $minutes < 60) {
                $cand = sprintf("%02d:%02d", $hours, $minutes);
                if ($cand > $best) $best = $cand;
            }
        } while ($nextPermutation($arr));
        return $best;
    }
}
