<?php
// LeetCode 0744 - Find Smallest Letter Greater Than Target
// https://leetcode.com/problems/find-smallest-letter-greater-than-target/

class Solution {
    function nextGreatestLetter($letters, $target) {
        $left = 0;
        $right = count($letters);
        while ($left < $right) {
            $mid = $left + intdiv($right - $left, 2);
            if ($letters[$mid] <= $target) $left = $mid + 1;
            else $right = $mid;
        }
        return $letters[$left % count($letters)];
    }
}
