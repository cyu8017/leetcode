<?php
// LeetCode 1086 - High Five
// https://leetcode.com/problems/high-five/

class Solution {
    /**
     * @param Integer[][] $items
     * @return Integer[][]
     */
    function highFive($items) {
        $scores = [];
        foreach ($items as $item) {
            $scores[$item[0]][] = $item[1];
        }
        ksort($scores);
        $ans = [];
        foreach ($scores as $studentId => $list) {
            rsort($list);
            $top = array_slice($list, 0, 5);
            $ans[] = [$studentId, intdiv(array_sum($top), 5)];
        }
        return $ans;
    }
}
