<?php
// LeetCode 2795 - Parallel Execution of Promises for Individual Results Retrieval
// https://leetcode.com/problems/parallel-execution-of-promises-for-individual-results-retrieval/

class Solution {
    function promiseAllSettled($functions) {
        $out = [];
        foreach ($functions as $fn) {
            try {
                $value = $fn();
                $out[] = ['status' => 'fulfilled', 'value' => $value];
            } catch (Throwable $e) {
                $out[] = ['status' => 'rejected', 'reason' => $e->getMessage()];
            }
        }
        return $out;
    }
}
