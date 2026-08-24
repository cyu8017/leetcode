<?php
// LeetCode 2968 - Apply Operations to Maximize Frequency Score
// https://leetcode.com/problems/apply-operations-to-maximize-frequency-score/

class Solution {
    private function costRange($nums, $pref, $l, $r) {
        $mid = ($l + $r) >> 1;
        $left = $nums[$mid] * ($mid - $l) - ($pref[$mid] - $pref[$l]);
        $right = ($pref[$r + 1] - $pref[$mid + 1]) - $nums[$mid] * ($r - $mid);
        return $left + $right;
    }

    function maxFrequencyScore($nums, $k) {
        sort($nums);
        $n = count($nums);
        $pref = array_fill(0, $n + 1, 0);
        for ($i = 0; $i < $n; $i++) $pref[$i + 1] = $pref[$i] + $nums[$i];
        $ans = 1;
        $left = 0;
        for ($right = 0; $right < $n; $right++) {
            while ($this->costRange($nums, $pref, $left, $right) > $k) $left++;
            $ans = max($ans, $right - $left + 1);
        }
        return $ans;
    }
}
