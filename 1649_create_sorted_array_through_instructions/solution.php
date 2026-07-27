<?php
// LeetCode 1649 - Create Sorted Array through Instructions
// https://leetcode.com/problems/create-sorted-array-through-instructions/

class Solution {
    /**
     * @param Integer[] $instructions
     * @return Integer
     */
    function createSortedArray($instructions) {
        $MOD = 1000000007;
        $size = (empty($instructions) ? 0 : max($instructions)) + 2;
        $bit = array_fill(0, $size + 1, 0);
        $query = function ($i) use (&$bit) {
            $s = 0;
            while ($i) {
                $s += $bit[$i];
                $i -= $i & -$i;
            }
            return $s;
        };
        $ans = 0;
        foreach ($instructions as $i => $x) {
            $ans = ($ans + min($query($x - 1), $i - $query($x))) % $MOD;
            $j = $x;
            while ($j <= $size) {
                $bit[$j]++;
                $j += $j & -$j;
            }
        }
        return $ans;
    }
}
