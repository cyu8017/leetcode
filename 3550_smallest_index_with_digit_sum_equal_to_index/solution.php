<?php
// LeetCode 3550 - Smallest Index With Digit Sum Equal to Index
// https://leetcode.com/problems/smallest-index-with-digit-sum-equal-to-index/

class Solution {
    function smallestIndex($nums) {
        for ($i = 0; $i < count($nums); $i++) {
            $x = $nums[$i];
            $s = 0;
            for (; $x > 0; $x = intdiv($x, 10)) $s += $x % 10;
            if ($s === $i) return $i;
        }
        return -1;
    }
}
