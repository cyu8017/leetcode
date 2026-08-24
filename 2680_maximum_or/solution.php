<?php
// LeetCode 2680 - Maximum OR
// https://leetcode.com/problems/maximum-or/

class Solution {
    function maximumOr($nums, $k) {
        $n = count($nums);
        $pref = array_fill(0, $n + 1, 0);
        $suf = array_fill(0, $n + 1, 0);
        for ($i = 0; $i < $n; $i++) $pref[$i + 1] = $pref[$i] | $nums[$i];
        for ($i = $n - 1; $i >= 0; $i--) $suf[$i] = $suf[$i + 1] | $nums[$i];
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            $cur = $pref[$i] | ($nums[$i] * (1 << $k)) | $suf[$i + 1];
            if ($cur > $ans) $ans = $cur;
        }
        return $ans;
    }
}
