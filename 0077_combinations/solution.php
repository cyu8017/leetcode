<?php
// LeetCode 0077 - Combinations
// https://leetcode.com/problems/combinations/

class Solution {
    /**
     * @param Integer $n
     * @param Integer $k
     * @return Integer[][]
     */
    function combine($n, $k) {
        $result = [];
        $path = [];

        $backtrack = function ($start) use (&$n, &$k, &$result, &$path, &$backtrack) {
            if (count($path) === $k) {
                $result[] = $path;
                return;
            }

            $remaining = $k - count($path);
            for ($i = $start; $i <= $n - $remaining + 1; $i++) {
                $path[] = $i;
                $backtrack($i + 1);
                array_pop($path);
            }
        };

        $backtrack(1);
        return $result;
    }
}
