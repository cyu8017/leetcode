<?php
// LeetCode 2323 - Find Minimum Time to Finish All Jobs II
// https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs-ii/

class Solution {
    function minimumTime($jobs, $workers) {
        sort($jobs);
        sort($workers);
        $ans = 0;
        $n = count($jobs);
        for ($i = 0; $i < $n; ++$i)
            $ans = max($ans, intdiv($jobs[$i] + $workers[$i] - 1, $workers[$i]));
        return $ans;
    }
}
