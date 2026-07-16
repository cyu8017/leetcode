<?php
// LeetCode 0517 - Super Washing Machines
// https://leetcode.com/problems/super-washing-machines/

class Solution {
    /**
     * @param Integer[] $machines
     * @return Integer
     */
    function findMinMoves($machines) {
        return $this->find_min_moves($machines);
    }

    /**
     * @param Integer[] $machines
     * @return Integer
     */
    function find_min_moves($machines) {
        $total = array_sum($machines);
        $count = count($machines);
        if ($total % $count !== 0) {
            return -1;
        }

        $target = intdiv($total, $count);
        $prefix = 0;
        $result = 0;

        foreach ($machines as $clothes) {
            $diff = $clothes - $target;
            $prefix += $diff;
            $result = max($result, abs($prefix), $diff);
        }

        return $result;
    }
}
