<?php
// LeetCode 3332 - Maximum Points Tourist Can Earn
// https://leetcode.com/problems/maximum-points-tourist-can-earn/

class Solution {
    function maxScore($n, $k, $stayScore, $travelScore) {
        $dp = array_fill(0, $n, 0);
        for ($day = 0; $day < $k; $day++) {
            $ndp = array_fill(0, $n, -(1 << 30));
            for ($dest = 0; $dest < $n; $dest++) {
                $best = -(1 << 30);
                for ($src = 0; $src < $n; $src++) {
                    $val = $dp[$src];
                    if ($src === $dest) $val += $stayScore[$day][$dest];
                    else $val += $travelScore[$src][$dest];
                    if ($val > $best) $best = $val;
                }
                $ndp[$dest] = $best;
            }
            $dp = $ndp;
        }
        $ans = $dp[0];
        for ($i = 1; $i < $n; $i++) if ($dp[$i] > $ans) $ans = $dp[$i];
        return $ans;
    }
}
