<?php
// LeetCode 2282 - Number of People That Can Be Seen in a Grid
// https://leetcode.com/problems/number-of-people-that-can-be-seen-in-a-grid/

class Solution {
    function solve($heights) {
        $m = count($heights);
        $n = count($heights[0]);
        $ans = [];
        for ($i = 0; $i < $m; $i++) $ans[$i] = array_fill(0, $n, 0);
        for ($i = 0; $i < $m; $i++) {
            $stack = [];
            for ($j = $n - 1; $j >= 0; $j--) {
                $cnt = 0;
                while (count($stack) && $heights[$i][$stack[count($stack) - 1]] < $heights[$i][$j]) {
                    array_pop($stack);
                    $cnt++;
                }
                if (count($stack)) $cnt++;
                $ans[$i][$j] += $cnt;
                while (count($stack) && $heights[$i][$stack[count($stack) - 1]] === $heights[$i][$j]) array_pop($stack);
                $stack[] = $j;
            }
        }
        for ($j = 0; $j < $n; $j++) {
            $stack = [];
            for ($i = $m - 1; $i >= 0; $i--) {
                $cnt = 0;
                while (count($stack) && $heights[$stack[count($stack) - 1]][$j] < $heights[$i][$j]) {
                    array_pop($stack);
                    $cnt++;
                }
                if (count($stack)) $cnt++;
                $ans[$i][$j] += $cnt;
                while (count($stack) && $heights[$stack[count($stack) - 1]][$j] === $heights[$i][$j]) array_pop($stack);
                $stack[] = $i;
            }
        }
        return $ans;
    }
}
