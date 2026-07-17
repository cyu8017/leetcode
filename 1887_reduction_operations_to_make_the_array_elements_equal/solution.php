<?php
// LeetCode 1887 - Reduction Operations to Make the Array Elements Equal
// https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function reductionOperations($nums) {
        sort($nums);
        $answer = 0;
        $rank = 0;

        for ($i = 1, $n = count($nums); $i < $n; $i++) {
            if ($nums[$i] !== $nums[$i - 1]) {
                $rank++;
            }
            $answer += $rank;
        }
        return $answer;
    }
}
