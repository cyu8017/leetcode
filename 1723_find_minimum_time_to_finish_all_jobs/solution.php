<?php
// LeetCode 1723 - Find Minimum Time to Finish All Jobs
// https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs/

class Solution {
    private $best;

    /**
     * @param Integer[] $jobs
     * @param Integer $k
     * @return Integer
     */
    function minimumTimeRequired($jobs, $k) {
        rsort($jobs);
        $loads = array_fill(0, $k, 0);
        $this->best = array_sum($jobs);
        $this->backtrack(0, $jobs, $loads, $k);
        return $this->best;
    }

    private function backtrack($i, $jobs, &$loads, $k) {
        if ($i === count($jobs)) {
            $this->best = min($this->best, max($loads));
            return;
        }
        $seen = [];
        for ($worker = 0; $worker < $k; $worker++) {
            if (isset($seen[$loads[$worker]])) {
                continue;
            }
            if ($loads[$worker] + $jobs[$i] >= $this->best) {
                continue;
            }
            $seen[$loads[$worker]] = true;
            $loads[$worker] += $jobs[$i];
            $this->backtrack($i + 1, $jobs, $loads, $k);
            $loads[$worker] -= $jobs[$i];
            if ($loads[$worker] === 0) {
                break;
            }
        }
    }
}
