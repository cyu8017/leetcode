<?php
// LeetCode 2866 - Beautiful Towers II
// https://leetcode.com/problems/beautiful-towers-ii/

class Solution {
    function maximumSumOfHeights($maxHeights) {
        $n = count($maxHeights);
        $left = array_fill(0, $n, 0);
        $st = [-1];
        $sum = 0;
        for ($i = 0; $i < $n; $i++) {
            while (count($st) > 1 && $maxHeights[$st[count($st) - 1]] >= $maxHeights[$i]) {
                $j = array_pop($st);
                $sum -= $maxHeights[$j] * ($j - $st[count($st) - 1]);
            }
            $sum += $maxHeights[$i] * ($i - $st[count($st) - 1]);
            $left[$i] = $sum;
            $st[] = $i;
        }
        $right = array_fill(0, $n, 0);
        $st = [$n];
        $sum = 0;
        for ($i = $n - 1; $i >= 0; $i--) {
            while (count($st) > 1 && $maxHeights[$st[count($st) - 1]] >= $maxHeights[$i]) {
                $j = array_pop($st);
                $sum -= $maxHeights[$j] * ($st[count($st) - 1] - $j);
            }
            $sum += $maxHeights[$i] * ($st[count($st) - 1] - $i);
            $right[$i] = $sum;
            $st[] = $i;
        }
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            $cand = $left[$i] + $right[$i] - $maxHeights[$i];
            if ($cand > $ans) $ans = $cand;
        }
        return $ans;
    }
}
