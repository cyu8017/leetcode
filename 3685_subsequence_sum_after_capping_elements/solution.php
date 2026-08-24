<?php
// LeetCode 3685 - Subsequence Sum After Capping Elements
// https://leetcode.com/problems/subsequence-sum-after-capping-elements/

class Solution {
    function subsequenceSumAfterCapping($nums, $k) {
        $n = count($nums);
        $sorted = $nums;
        sort($sorted);
        $ans = array_fill(0, $n, false);
        $reach = array_fill(0, $k + 1, false);
        $reach[0] = true;
        $idx = 0;
        for ($x = 1; $x <= $n; $x++) {
            while ($idx < $n && $sorted[$idx] <= $x) {
                $v = $sorted[$idx];
                for ($s = $k; $s >= $v; $s--) {
                    if ($reach[$s - $v]) $reach[$s] = true;
                }
                $idx++;
            }
            $tmp = $reach;
            $rem = $n - $idx;
            for ($s = 0; $s <= $k; $s++) {
                if (!$reach[$s]) continue;
                for ($t = 1; $t <= $rem && $s + $t * $x <= $k; $t++) $tmp[$s + $t * $x] = true;
            }
            $ans[$x - 1] = $tmp[$k];
        }
        return $ans;
    }
}
