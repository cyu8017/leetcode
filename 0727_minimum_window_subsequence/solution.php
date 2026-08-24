<?php
// LeetCode 0727 - Minimum Window Subsequence
// https://leetcode.com/problems/minimum-window-subsequence/

class Solution {
    function minWindow($s1, $s2) {
        $m = strlen($s1);
        $n = strlen($s2);
        $best = '';
        $i = 0;
        while ($i < $m) {
            $j = 0;
            $k = $i;
            while ($k < $m && $j < $n) {
                if ($s1[$k] === $s2[$j]) $j++;
                $k++;
            }
            if ($j < $n) break;
            $end = $k - 1;
            $j = $n - 1;
            $k = $end;
            while ($j >= 0) {
                if ($s1[$k] === $s2[$j]) $j--;
                $k--;
            }
            $start = $k + 1;
            if (strlen($best) === 0 || $end - $start + 1 < strlen($best)) $best = substr($s1, $start, $end - $start + 1);
            $i = $start + 1;
        }
        return $best;
    }
}
