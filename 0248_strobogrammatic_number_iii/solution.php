<?php
// LeetCode 0248 - Strobogrammatic Number III
// https://leetcode.com/problems/strobogrammatic-number-iii/

class Solution {
    private $pairs = [
        ["0", "0"],
        ["1", "1"],
        ["6", "9"],
        ["8", "8"],
        ["9", "6"],
    ];

    /**
     * @param String $low
     * @param String $high
     * @return Integer
     */
    function strobogrammaticInRange($low, $high) {
        $lowValue = (int)$low;
        $highValue = (int)$high;
        $count = 0;

        for ($length = strlen($low); $length <= strlen($high); $length++) {
            foreach ($this->build(0, $length - 1) as $value) {
                $numeric = (int)$value;
                if ($lowValue <= $numeric && $numeric <= $highValue) {
                    $count++;
                }
            }
        }
        return $count;
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
