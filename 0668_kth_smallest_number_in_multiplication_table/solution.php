<?php
// LeetCode 0668 - Kth Smallest Number in Multiplication Table
// https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/

class Solution {
    function findKthNumber($m, $n, $k) {
        $countLe = function($x) use ($m, $n) {
            $count = 0;
            for ($row = 1; $row <= $m; ++$row) $count += min(intdiv($x, $row), $n);
            return $count;
        };
        $lo = 1;
        $hi = $m * $n;
        while ($lo < $hi) {
            $mid = $lo + intdiv($hi - $lo, 2);
            if ($countLe($mid) >= $k) $hi = $mid;
            else $lo = $mid + 1;
        }
        return $lo;
    }
}
