<?php
// LeetCode 2659 - Make Array Empty
// https://leetcode.com/problems/make-array-empty/

class Solution {
    function countOperationsToEmptyArray($nums) {
        $n = count($nums);
        $idx = range(0, $n - 1);
        usort($idx, function($a, $b) use ($nums) { return $nums[$a] <=> $nums[$b]; });
        $ans = $n;
        for ($i = 1; $i < $n; $i++) {
            if ($idx[$i] < $idx[$i - 1]) $ans += $n - $i;
        }
        return $ans;
    }
}
