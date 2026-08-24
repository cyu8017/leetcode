<?php
// LeetCode 3516 - Find Closest Person
// https://leetcode.com/problems/find-closest-person/

class Solution {
    function findClosest($x, $y, $z) {
        $a = abs($x - $z);
        $b = abs($y - $z);
        if ($a === $b) return 0;
        return $a < $b ? 1 : 2;
    }
}
