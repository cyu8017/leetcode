<?php
// LeetCode 2059 - Minimum Operations to Convert Number
// https://leetcode.com/problems/minimum-operations-to-convert-number/

class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $start
     * @param Integer $goal
     * @return Integer
     */
    function minimumOperations($nums, $start, $goal) {
        if ($start === $goal) return 0;
        $vis = [$start => true];
        $q = [$start];
        $steps = 0;
        while ($q) {
            $steps++;
            $sz = count($q);
            while ($sz-- > 0) {
                $cur = array_shift($q);
                foreach ($nums as $x) {
                    foreach ([$cur + $x, $cur - $x, $cur ^ $x] as $nxt) {
                        if ($nxt === $goal) return $steps;
                        if ($nxt >= 0 && $nxt <= 1000 && !isset($vis[$nxt])) {
                            $vis[$nxt] = true;
                            $q[] = $nxt;
                        }
                    }
                }
            }
        }
        return -1;
    }
}
