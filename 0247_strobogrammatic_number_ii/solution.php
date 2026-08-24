<?php
// LeetCode 0247 - Strobogrammatic Number II
// https://leetcode.com/problems/strobogrammatic-number-ii/

class Solution {
    private $pairs = [
        ["0", "0"],
        ["1", "1"],
        ["6", "9"],
        ["8", "8"],
        ["9", "6"],
    ];

    /**
     * @param Integer $n
     * @return String[]
     */
    function findStrobogrammatic($n) {
        return $this->build(0, $n - 1);
    }

    private function build($left, $right) {
        if ($left > $right) {
            return [""];
        }
        if ($left === $right) {
            return ["0", "1", "8"];
        }

        $result = [];
        foreach ($this->pairs as $pair) {
            [$start, $end] = $pair;
            if ($left === 0 && $start === "0") {
                continue;
            }
            foreach ($this->build($left + 1, $right - 1) as $middle) {
                $result[] = $start . $middle . $end;
            }
        }
        return $result;
    }
}
