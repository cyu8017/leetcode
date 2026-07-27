<?php
// LeetCode 1679 - Max Number of K-Sum Pairs
// https://leetcode.com/problems/max-number-of-k-sum-pairs/

class Solution {
    function maxOperations($nums, $k) {
        $c = [];
        $ans = 0;
        foreach ($nums as $x) {
            $need = $k - $x;
            if (($c[$need] ?? 0) > 0) {
                $c[$need]--;
                $ans++;
            } else {
                $c[$x] = ($c[$x] ?? 0) + 1;
            }
        }
        return $ans;
    }
}
