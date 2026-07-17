<?php
// LeetCode 1899 - Merge Triplets to Form Target Triplet
// https://leetcode.com/problems/merge-triplets-to-form-target-triplet/

class Solution {
    /**
     * @param Integer[][] $triplets
     * @param Integer[] $target
     * @return Boolean
     */
    function mergeTriplets($triplets, $target) {
        $merged = [0, 0, 0];
        foreach ($triplets as $triplet) {
            [$a, $b, $c] = $triplet;
            if ($a <= $target[0] && $b <= $target[1] && $c <= $target[2]) {
                $merged[0] = max($merged[0], $a);
                $merged[1] = max($merged[1], $b);
                $merged[2] = max($merged[2], $c);
            }
        }
        return $merged === $target;
    }
}
