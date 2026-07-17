<?php
// LeetCode 1806 - Minimum Number of Operations to Reinitialize a Permutation
// https://leetcode.com/problems/minimum-number-of-operations-to-reinitialize-a-permutation/

class Solution {
    /**
     * @param Integer $n
     * @return Integer
     */
    function reinitializePermutation($n) {
        $perm = range(0, $n - 1);
        $target = $perm;
        $operations = 0;

        while (true) {
            $newPerm = array_fill(0, $n, 0);
            for ($i = 0; $i < $n; $i++) {
                if ($i % 2 === 0) {
                    $newPerm[$i] = $perm[intdiv($i, 2)];
                } else {
                    $newPerm[$i] = $perm[intdiv($n, 2) + intdiv($i - 1, 2)];
                }
            }
            $perm = $newPerm;
            $operations++;
            if ($perm === $target) {
                return $operations;
            }
        }
    }
}
