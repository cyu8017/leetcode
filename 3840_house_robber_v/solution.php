<?php
// LeetCode 3840 - House Robber V
// https://leetcode.com/problems/house-robber-v/

class Solution {
    function rob($nums, $colors) {
        $n = count($nums);
        $f = 0;
        $g = $nums[0];
        for ($i = 1; $i < $n; $i++) {
            if ($colors[$i - 1] === $colors[$i]) {
                $nf = max($f, $g);
                $g = $f + $nums[$i];
                $f = $nf;
            } else {
                $nf = max($f, $g);
                $g = $nf + $nums[$i];
                $f = $nf;
            }
        }
        return max($f, $g);
    }
}
