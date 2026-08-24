<?php
// LeetCode 3874 - Valid Subarrays With Exactly One Peak
// https://leetcode.com/problems/valid-subarrays-with-exactly-one-peak/

class Solution {
    function validSubarrays($nums, $k) {
        $n = count($nums);
        $peaks = [];
        for ($i = 1; $i < $n - 1; $i++) {
            if ($nums[$i] > $nums[$i - 1] && $nums[$i] > $nums[$i + 1]) $peaks[] = $i;
        }
        $ans = 0;
        $pn = count($peaks);
        for ($j = 0; $j < $pn; $j++) {
            $p = $peaks[$j];
            $leftMin = max($p - $k, 0);
            if ($j > 0) $leftMin = max($leftMin, $peaks[$j - 1] + 1);
            $rightMax = min($p + $k, $n - 1);
            if ($j < $pn - 1) $rightMax = min($rightMax, $peaks[$j + 1] - 1);
            $ans += ($p - $leftMin + 1) * ($rightMax - $p + 1);
        }
        return $ans;
    }
}
