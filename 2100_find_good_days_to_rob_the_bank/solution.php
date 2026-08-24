<?php
// LeetCode 2100 - Find Good Days to Rob the Bank
// https://leetcode.com/problems/find-good-days-to-rob-the-bank/

class Solution {
    /**
     * @param Integer[] $security
     * @param Integer $time
     * @return Integer[]
     */
    function goodDaysToRobBank($security, $time) {
        $n = count($security);
        if ($time === 0) return range(0, $n - 1);
        $left = array_fill(0, $n, 0);
        $right = array_fill(0, $n, 0);
        for ($i = 1; $i < $n; $i++) {
            if ($security[$i] <= $security[$i - 1]) $left[$i] = $left[$i - 1] + 1;
        }
        for ($i = $n - 2; $i >= 0; $i--) {
            if ($security[$i] <= $security[$i + 1]) $right[$i] = $right[$i + 1] + 1;
        }
        $ans = [];
        for ($i = $time; $i < $n - $time; $i++) {
            if ($left[$i] >= $time && $right[$i] >= $time) $ans[] = $i;
        }
        return $ans;
    }
}
