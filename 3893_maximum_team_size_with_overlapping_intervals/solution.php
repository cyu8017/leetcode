<?php
// LeetCode 3893 - Maximum Team Size With Overlapping Intervals
// https://leetcode.com/problems/maximum-team-size-with-overlapping-intervals/

class Solution {
    function UpperBound($a, $x) {
        $lo = 0;
        $hi = count($a);
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi, 2);
            if ($a[$mid] <= $x) $lo = $mid + 1;
            else $hi = $mid;
        }
        return $lo;
    }
    function maximumTeamSize($startTime, $endTime) {
        $n = count($startTime);
        $st = $startTime;
        $en = $endTime;
        sort($st);
        sort($en);
        $ans = 0;
        for ($t = 0; $t < $n; $t++) {
            $l = $startTime[$t];
            $r = $endTime[$t];
            $i = $this->UpperBound($en, $l - 1);
            $j = $this->UpperBound($st, $r);
            $ans = max($ans, $j - $i);
        }
        return $ans;
    }
}
