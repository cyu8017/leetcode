<?php
// LeetCode 0254 - Factor Combinations
// https://leetcode.com/problems/factor-combinations/

class Solution {
    /**
     * @param Integer $n
     * @return Integer[][]
     */
    function getFactors($n) {
        $result = [];
        $path = [];
        $this->backtrack($n, 2, $path, $result);
        return $result;
    }

    private function backtrack($remain, $start, &$path, &$result) {
        if ($start > $remain) {
            if (count($path) > 1) {
                $result[] = $path;
            }
            return;
        }

        for ($factor = $start; $factor * $factor <= $remain; $factor++) {
            if ($remain % $factor === 0) {
                $path[] = $factor;
                $this->backtrack(intdiv($remain, $factor), $factor, $path, $result);
                array_pop($path);
            }
        }

        if (!empty($path)) {
            $path[] = $remain;
            if (count($path) > 1) {
                $result[] = $path;
            }
            array_pop($path);
        }
    }
}
