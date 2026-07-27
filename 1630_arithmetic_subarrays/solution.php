<?php
// LeetCode 1630 - Arithmetic Subarrays
// https://leetcode.com/problems/arithmetic-subarrays/

class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer[] $l
     * @param Integer[] $r
     * @return Boolean[]
     */
    function checkArithmeticSubarrays($nums, $l, $r) {
        $ans = [];
        $m = count($l);
        for ($i = 0; $i < $m; $i++) {
            $x = array_slice($nums, $l[$i], $r[$i] - $l[$i] + 1);
            sort($x);
            $ok = count($x) < 3;
            if (!$ok) {
                $diff = $x[1] - $x[0];
                $ok = true;
                for ($j = 2; $j < count($x); $j++) {
                    if ($x[$j] - $x[$j - 1] !== $diff) {
                        $ok = false;
                        break;
                    }
                }
            }
            $ans[] = $ok;
        }
        return $ans;
    }
}
