<?php
// LeetCode 3511 - Make a Positive Array
// https://leetcode.com/problems/make-a-positive-array/

class Solution {
    function makeArrayPositive($nums) {
        $ans = 0;
        $l = -1;
        $preMx = 0;
        $s = 0;
        $n = count($nums);
        for ($r = 0; $r < $n; $r++) {
            $s += $nums[$r];
            if ($r - $l > 2 && $s <= $preMx) {
                $ans++;
                $l = $r;
                $preMx = 0;
                $s = 0;
            } else if ($r - $l >= 2) {
                $preMx = max($preMx, $s - $nums[$r] - $nums[$r - 1]);
            }
        }
        return $ans;
    }
}
