<?php
// LeetCode 2856 - Minimum Array Length After Pair Removals
// https://leetcode.com/problems/minimum-array-length-after-pair-removals/

class Solution {
    function minLengthAfterRemovals($nums) {
        $n = count($nums);
        $freq = [];
        $mx = 0;
        foreach ($nums as $v) {
            if (!isset($freq[$v])) $freq[$v] = 0;
            $freq[$v]++;
            if ($freq[$v] > $mx) $mx = $freq[$v];
        }
        if ($mx <= intdiv($n, 2)) return $n % 2;
        return 2 * $mx - $n;
    }
}
