<?php
// LeetCode 0532 - K-diff Pairs in an Array
// https://leetcode.com/problems/k-diff-pairs-in-an-array/

class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer
     */
    function findPairs($nums, $k) {
        return $this->find_pairs($nums, $k);
    }

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer
     */
    function find_pairs($nums, $k) {
        if ($k < 0) {
            return 0;
        }

        $freq = [];
        foreach ($nums as $num) {
            if (!isset($freq[$num])) {
                $freq[$num] = 0;
            }
            $freq[$num]++;
        }

        $pairs = 0;
        foreach ($freq as $num => $count) {
            if ($k === 0) {
                if ($count > 1) {
                    $pairs++;
                }
            } elseif (isset($freq[$num + $k])) {
                $pairs++;
            }
        }
        return $pairs;
    }
}
