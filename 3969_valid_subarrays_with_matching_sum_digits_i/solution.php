<?php
// LeetCode 3969 - Valid Subarrays With Matching Sum Digits I
// https://leetcode.com/problems/valid-subarrays-with-matching-sum-digits-i/

class Solution {
    function countValidSubarrays($nums, $x) {
        $n = count($nums);
        $ans = 0;
        for ($l = 0; $l < $n; $l++) {
            $s = 0;
            for ($r = $l; $r < $n; $r++) {
                $s += $nums[$r];
                if ($s % 10 === $x) {
                    $t = strval($s);
                    if (intval($t[0]) === $x) $ans++;
                }
            }
        }
        return $ans;
    }
}
