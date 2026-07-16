<?php
// LeetCode 0506 - Relative Ranks
// https://leetcode.com/problems/relative-ranks/

class Solution {
    /**
     * @param Integer[] $score
     * @return String[]
     */
    function findRelativeRanks($score) {
        return $this->find_relative_ranks($score);
    }

    /**
     * @param Integer[] $score
     * @return String[]
     */
    function find_relative_ranks($score) {
        $medals = [
            1 => "Gold Medal",
            2 => "Silver Medal",
            3 => "Bronze Medal",
        ];
        $order = range(0, count($score) - 1);
        usort($order, fn($left, $right) => $score[$right] <=> $score[$left]);
        $result = array_fill(0, count($score), "");
        foreach ($order as $rank => $index) {
            $result[$index] = $medals[$rank + 1] ?? (string)($rank + 1);
        }
        return $result;
    }
}
