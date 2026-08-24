<?php
// LeetCode 0659 - Split Array into Consecutive Subsequences
// https://leetcode.com/problems/split-array-into-consecutive-subsequences/

class Solution {
    function isPossible($nums) {
        $freq = [];
        $tails = [];
        foreach ($nums as $num) $freq[$num] = ($freq[$num] ?? 0) + 1;
        foreach ($nums as $num) {
            if (($freq[$num] ?? 0) === 0) continue;
            $freq[$num] = $freq[$num] - 1;
            if (($tails[$num - 1] ?? 0) > 0) {
                $tails[$num - 1] = $tails[$num - 1] - 1;
                $tails[$num] = ($tails[$num] ?? 0) + 1;
            } elseif (($freq[$num + 1] ?? 0) > 0 && ($freq[$num + 2] ?? 0) > 0) {
                $freq[$num + 1] = $freq[$num + 1] - 1;
                $freq[$num + 2] = $freq[$num + 2] - 1;
                $tails[$num + 2] = ($tails[$num + 2] ?? 0) + 1;
            } else {
                return false;
            }
        }
        return true;
    }
}
