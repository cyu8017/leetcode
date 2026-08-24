<?php
// LeetCode 3282 - Reach End of Array With Max Score
// https://leetcode.com/problems/reach-end-of-array-with-max-score/

class Solution {
    function findMaximumScore($nums) {
        $ans = 0;
        $maxV = 0;
        $n = count($nums);
        for ($i = 0; $i < $n - 1; $i++) {
            if ($nums[$i] > $maxV) $maxV = $nums[$i];
            $ans += $maxV;
        }
        return $ans;
    }
}
