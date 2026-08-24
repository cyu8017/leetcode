<?php
// LeetCode 2352 - Equal Row and Column Pairs
// https://leetcode.com/problems/equal-row-and-column-pairs/

class Solution {
    function equalPairs($grid) {
        $n = count($grid);
        $freq = [];
        for ($i = 0; $i < $n; $i++) {
            $key = implode(',', $grid[$i]);
            $freq[$key] = ($freq[$key] ?? 0) + 1;
        }
        $ans = 0;
        for ($j = 0; $j < $n; $j++) {
            $col = [];
            for ($i = 0; $i < $n; $i++) $col[] = $grid[$i][$j];
            $ans += $freq[implode(',', $col)] ?? 0;
        }
        return $ans;
    }
}
