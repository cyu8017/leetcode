<?php
class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function findMaximums($nums) {
        $n = count($nums);
        $left = array_fill(0, $n, -1);
        $right = array_fill(0, $n, $n);
        $stack = [];
        for ($i = 0; $i < $n; $i++) {
            $x = $nums[$i];
            while (!empty($stack) && $nums[end($stack)] >= $x) {
                array_pop($stack);
            }
            $left[$i] = empty($stack) ? -1 : end($stack);
            $stack[] = $i;
        }
        $stack = [];
        for ($i = $n - 1; $i >= 0; $i--) {
            while (!empty($stack) && $nums[end($stack)] >= $nums[$i]) {
                array_pop($stack);
            }
            $right[$i] = empty($stack) ? $n : end($stack);
            $stack[] = $i;
        }

        $ans = array_fill(0, $n, 0);
        for ($i = 0; $i < $n; $i++) {
            $x = $nums[$i];
            $length = $right[$i] - $left[$i] - 1;
            $ans[$length - 1] = max($ans[$length - 1], $x);
        }
        for ($i = $n - 2; $i >= 0; $i--) {
            $ans[$i] = max($ans[$i], $ans[$i + 1]);
        }
        return $ans;
    }
}
