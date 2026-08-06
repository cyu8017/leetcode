<?php
// LeetCode 1235 - Maximum Profit in Job Scheduling
// https://leetcode.com/problems/maximum-profit-in-job-scheduling/

class Solution {
    /**
     * @param Integer[] $startTime
     * @param Integer[] $endTime
     * @param Integer[] $profit
     * @return Integer
     */
    function jobScheduling($startTime, $endTime, $profit) {
        $jobs = [];
        $n = count($startTime);
        for ($i = 0; $i < $n; $i++) $jobs[] = [$endTime[$i], $startTime[$i], $profit[$i]];
        usort($jobs, fn($a, $b) => $a[0] <=> $b[0]);
        $ends = [0];
        $dp = [0];
        foreach ($jobs as [$end, $start, $gain]) {
            $lo = 0; $hi = count($ends);
            while ($lo < $hi) {
                $mid = ($lo + $hi) >> 1;
                if ($ends[$mid] <= $start) $lo = $mid + 1;
                else $hi = $mid;
            }
            $i = $lo - 1;
            $ends[] = $end;
            $dp[] = max(end($dp), $dp[$i] + $gain);
        }
        return end($dp);
    }
}
