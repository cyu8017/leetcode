<?php
// LeetCode 2772 - Apply Operations to Make All Array Elements Equal to Zero
// https://leetcode.com/problems/apply-operations-to-make-all-array-elements-equal-to-zero/

class Solution {
    function checkArray($nums, $k) {
        $n = count($nums);
        $diff = array_fill(0, $n + 1, 0);
        $cur = 0;
        for ($i = 0; $i < $n; $i++) {
            $cur += $diff[$i];
            $need = $nums[$i] - $cur;
            if ($need < 0) return false;
            if ($need > 0) {
                if ($i + $k > $n) return false;
                $cur += $need;
                $diff[$i + $k] -= $need;
            }
        }
        return true;
    }
}
