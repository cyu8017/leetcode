<?php
// LeetCode 0826 - Most Profit Assigning Work
// https://leetcode.com/problems/most-profit-assigning-work/

class Solution {
    /**
     * @param Integer[] $difficulty
     * @param Integer[] $profit
     * @param Integer[] $worker
     * @return Integer
     */
    function maxProfitAssignment($difficulty, $profit, $worker) {
        $jobs = [];
        $n = count($difficulty);
        for ($i = 0; $i < $n; $i++) $jobs[] = [$difficulty[$i], $profit[$i]];
        usort($jobs, function($a, $b) { return $a[0] <=> $b[0]; });
        sort($worker);
        $ans = 0;
        $best = 0;
        $i = 0;
        foreach ($worker as $ability) {
            while ($i < count($jobs) && $jobs[$i][0] <= $ability) {
                $best = max($best, $jobs[$i][1]);
                $i++;
            }
            $ans += $best;
        }
        return $ans;
    }
}
