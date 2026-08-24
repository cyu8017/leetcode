<?php
// LeetCode 3833 - Count Dominant Indices
// https://leetcode.com/problems/count-dominant-indices/

class Solution {
    function dominantIndices($nums) {
        $n = count($nums);
        $ans = 0;
        $suf = $nums[$n - 1];
        for ($i = $n - 2; $i >= 0; $i--) {
            if ($nums[$i] * ($n - $i - 1) > $suf) $ans++;
            $suf += $nums[$i];
        }
        return $ans;
    }
}
