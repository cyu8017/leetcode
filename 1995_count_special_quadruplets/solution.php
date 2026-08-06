<?php
// LeetCode 1995 - Count Special Quadruplets
// https://leetcode.com/problems/count-special-quadruplets/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function countQuadruplets($nums) {
        $n = count($nums);
        $ans = 0;
        for ($a = 0; $a < $n; $a++) {
            for ($b = $a + 1; $b < $n; $b++) {
                for ($c = $b + 1; $c < $n; $c++) {
                    $s = $nums[$a] + $nums[$b] + $nums[$c];
                    for ($d = $c + 1; $d < $n; $d++) {
                        if ($nums[$d] === $s) {
                            $ans++;
                        }
                    }
                }
            }
        }
        return $ans;
    }
}
