<?php
// LeetCode 2319 - Check if Matrix Is X-Matrix
// https://leetcode.com/problems/check-if-matrix-is-x-matrix/

class Solution {
    function checkXMatrix($grid) {
        $n = count($grid);
        for ($i = 0; $i < $n; ++$i) {
            for ($j = 0; $j < $n; ++$j) {
                $diag = ($i === $j || $i + $j === $n - 1);
                if ($diag) { if ($grid[$i][$j] === 0) return false; }
                elseif ($grid[$i][$j] !== 0) return false;
            }
        }
        return true;
    }
}
