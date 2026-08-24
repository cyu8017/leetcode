<?php
// LeetCode 2584 - Split the Array to Make Coprime Products
// https://leetcode.com/problems/split-the-array-to-make-coprime-products/

class Solution {
    function findValidSplit($nums) {
        $first = [];
        $last = [];
        $factorize = function($x, $idx) use (&$first, &$last) {
            for ($p = 2; $p * $p <= $x; $p++) {
                if ($x % $p === 0) {
                    if (!isset($first[$p])) $first[$p] = $idx;
                    $last[$p] = $idx;
                    while ($x % $p === 0) $x = intdiv($x, $p);
                }
            }
            if ($x > 1) {
                if (!isset($first[$x])) $first[$x] = $idx;
                $last[$x] = $idx;
            }
        };
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) $factorize($nums[$i], $i);
        $far = 0;
        for ($i = 0; $i < $n - 1; $i++) {
            $x = $nums[$i];
            for ($p = 2; $p * $p <= $x; $p++) {
                if ($x % $p === 0) {
                    if ($last[$p] > $far) $far = $last[$p];
                    while ($x % $p === 0) $x = intdiv($x, $p);
                }
            }
            if ($x > 1 && $last[$x] > $far) $far = $last[$x];
            if ($far === $i) return $i;
        }
        return -1;
    }
}
