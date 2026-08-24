<?php
// LeetCode 2442 - Count Number of Distinct Integers After Reverse Operations
// https://leetcode.com/problems/count-number-of-distinct-integers-after-reverse-operations/

class Solution {
    function countDistinctIntegers($nums) {
        $rev = function ($x) {
            $r = 0;
            while ($x > 0) {
                $r = $r * 10 + $x % 10;
                $x = intdiv($x, 10);
            }
            return $r;
        };
        $seen = [];
        foreach ($nums as $x) {
            $seen[$x] = true;
            $seen[$rev($x)] = true;
        }
        return count($seen);
    }
}
