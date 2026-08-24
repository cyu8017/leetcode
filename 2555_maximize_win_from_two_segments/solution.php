<?php
// LeetCode 2555 - Maximize Win From Two Segments
// https://leetcode.com/problems/maximize-win-from-two-segments/

class Solution {
    function maximizeWin($prizePositions, $k) {
        $n = count($prizePositions);
        $dp = array_fill(0, $n + 1, 0);
        $ans = 0;
        $left = 0;
        for ($right = 0; $right < $n; $right++) {
            while ($prizePositions[$right] - $prizePositions[$left] > $k) $left++;
            $cur = $right - $left + 1;
            if ($dp[$left] + $cur > $ans) $ans = $dp[$left] + $cur;
            $best = $cur;
            if ($dp[$right] > $best) $best = $dp[$right];
            $dp[$right + 1] = $best;
        }
        return $ans;
    }
}
