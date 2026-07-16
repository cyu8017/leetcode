<?php
// LeetCode 0526 - Beautiful Arrangement
// https://leetcode.com/problems/beautiful-arrangement/

class Solution {
    /**
     * @param Integer $n
     * @return Integer
     */
    function countArrangement($n) {
        return $this->count_arrangement($n);
    }

    /**
     * @param Integer $n
     * @return Integer
     */
    function count_arrangement($n) {
        $count = 0;
        $backtrack = function ($index, $used) use (&$backtrack, $n, &$count) {
            if ($index === $n + 1) {
                $count++;
                return;
            }
            for ($num = 1; $num <= $n; $num++) {
                if (isset($used[$num])) {
                    continue;
                }
                if ($index % $num !== 0 && $num % $index !== 0) {
                    continue;
                }
                $used[$num] = true;
                $backtrack($index + 1, $used);
                unset($used[$num]);
            }
        };
        $backtrack(1, []);
        return $count;
    }
}
