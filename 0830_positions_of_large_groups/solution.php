<?php
// LeetCode 0830 - Positions of Large Groups
// https://leetcode.com/problems/positions-of-large-groups/

class Solution {
    /**
     * @param String $s
     * @return Integer[][]
     */
    function largeGroupPositions($s) {
        $ans = [];
        $n = strlen($s);
        $i = 0;
        while ($i < $n) {
            $j = $i;
            while ($j < $n && $s[$j] === $s[$i]) $j++;
            if ($j - $i >= 3) $ans[] = [$i, $j - 1];
            $i = $j;
        }
        return $ans;
    }
}
