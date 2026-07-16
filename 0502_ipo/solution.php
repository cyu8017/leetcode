<?php
// LeetCode 0502 - IPO
// https://leetcode.com/problems/ipo/

class Solution {
    /**
     * @param Integer $k
     * @param Integer $w
     * @param Integer[] $profits
     * @param Integer[] $capital
     * @return Integer
     */
    function findMaximizedCapital($k, $w, $profits, $capital) {
        return $this->find_maximized_capital($k, $w, $profits, $capital);
    }

    /**
     * @param Integer $k
     * @param Integer $w
     * @param Integer[] $profits
     * @param Integer[] $capital
     * @return Integer
     */
    function find_maximized_capital($k, $w, $profits, $capital) {
        $projects = [];
        foreach ($capital as $index => $projectCapital) {
            $projects[] = [$projectCapital, $profits[$index]];
        }
        usort($projects, fn($left, $right) => $left[0] <=> $right[0]);

        $available = new SplMaxHeap();
        $index = 0;
        for ($round = 0; $round < $k; $round++) {
            while ($index < count($projects) && $projects[$index][0] <= $w) {
                $available->insert($projects[$index][1]);
                $index++;
            }
            if ($available->isEmpty()) {
                break;
            }
            $w += $available->extract();
        }
        return $w;
    }
}
