<?php
// LeetCode 0565 - Array Nesting
// https://leetcode.com/problems/array-nesting/

class Solution {
    function arrayNesting($nums) {
        $best = 0;
        for ($i = 0; $i < count($nums); ++$i) {
            if ($nums[$i] < 0) continue;
            $length = 0;
            $j = $i;
            while ($nums[$j] >= 0) {
                $nxt = $nums[$j];
                $nums[$j] = -1;
                $j = $nxt;
                ++$length;
            }
            $best = max($best, $length);
        }
        return $best;
    }
}
