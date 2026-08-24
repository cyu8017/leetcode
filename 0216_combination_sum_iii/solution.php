<?php
// LeetCode 0216 - Combination Sum III
// https://leetcode.com/problems/combination-sum-iii/

class Solution {
    function combinationSum3($k, $n) {
        $result = [];
        $path = [];
        $this->backtrack(1, $k, $n, $path, $result);
        return $result;
    }

    private function backtrack($start, $k, $remaining, &$path, &$result) {
        if (count($path) === $k) {
            if ($remaining === 0) {
                $result[] = $path;
            }
            return;
        }
        if ($remaining <= 0 || count($path) >= $k) {
            return;
        }
        for ($num = $start; $num <= 9; $num++) {
            if ($num > $remaining) {
                break;
            }
            $path[] = $num;
            $this->backtrack($num + 1, $k, $remaining - $num, $path, $result);
            array_pop($path);
        }
    }
}
