<?php
// LeetCode 3209 - Number of Subarrays With AND Value of K
// https://leetcode.com/problems/number-of-subarrays-with-and-value-of-k/

class Solution {
    function countSubarrays($nums, $k) {
        $pre = [];
        $ans = 0;
        foreach ($nums as $x) {
            $cur = [];
            foreach ($pre as $key => $val) {
                $nk = $x & $key;
                $cur[$nk] = ($cur[$nk] ?? 0) + $val;
            }
            $cur[$x] = ($cur[$x] ?? 0) + 1;
            $ans += $cur[$k] ?? 0;
            $pre = $cur;
        }
        return $ans;
    }
}
