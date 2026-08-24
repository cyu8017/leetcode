<?php
// LeetCode 3771 - Total Score of Dungeon Runs
// https://leetcode.com/problems/total-score-of-dungeon-runs/

class Solution {
    function totalScore($hp, $damage, $requirement) {
        $n = count($damage);
        $prefix = array_fill(0, $n + 1, 0);
        for ($i = 0; $i < $n; $i++) $prefix[$i + 1] = $prefix[$i] + $damage[$i];
        $answer = $n * ($n + 1) / 2;
        for ($j = 1; $j <= $n; $j++) {
            $threshold = $prefix[$j] + ($requirement[$j - 1] - $hp);
            $lo = 0;
            $hi = $j;
            while ($lo < $hi) {
                $mid = ($lo + $hi) >> 1;
                if ($prefix[$mid] < $threshold) $lo = $mid + 1;
                else $hi = $mid;
            }
            $answer -= $lo;
        }
        return $answer;
    }
}
