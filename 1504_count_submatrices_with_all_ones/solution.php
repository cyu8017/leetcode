<?php
// LeetCode 1504 - Count Submatrices With All Ones
// https://leetcode.com/problems/count-submatrices-with-all-ones/

class Solution {
    /**
     * @param Integer[][] $mat
     * @return Integer
     */
    function numSubmat($mat) {
        $ans = 0;
        $cols = count($mat[0]);
        $heights = array_fill(0, $cols, 0);
        foreach ($mat as $row) {
            for ($j = 0; $j < $cols; $j++) {
                $heights[$j] = $row[$j] ? $heights[$j] + 1 : 0;
            }
            $stack = [];
            $running = 0;
            foreach ($heights as $h) {
                $count = 1;
                while (!empty($stack) && $stack[count($stack) - 1][0] >= $h) {
                    [$old, $width] = array_pop($stack);
                    $running -= $old * $width;
                    $count += $width;
                }
                $stack[] = [$h, $count];
                $running += $h * $count;
                $ans += $running;
            }
        }
        return $ans;
    }
}
