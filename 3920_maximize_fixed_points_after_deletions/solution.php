<?php
// LeetCode 3920 - Maximize Fixed Points After Deletions
// https://leetcode.com/problems/maximize-fixed-points-after-deletions/

class Solution {
    function maxFixedPoints($nums) {
        $tails = [];
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) {
            if ($i < $nums[$i]) continue;
            $d = $i - $nums[$i];
            $lo = 0;
            $hi = count($tails);
            while ($lo < $hi) {
                $mid = ($lo + $hi) >> 1;
                if ($tails[$mid] < $d) $lo = $mid + 1;
                else $hi = $mid;
            }
            if ($lo === count($tails)) $tails[] = $d;
            else $tails[$lo] = $d;
        }
        return count($tails);
    }
}
