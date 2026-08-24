<?php
// LeetCode 0163 - Missing Ranges
// https://leetcode.com/problems/missing-ranges/

class Solution {
    function findMissingRanges(array $nums, int $lower, int $upper): array {
        $result = [];
        $previous = $lower - 1;
        foreach (array_merge($nums, [$upper + 1]) as $number) {
            if ($number - $previous >= 2) $result[] = [$previous + 1, $number - 1];
            $previous = $number;
        }
        return $result;
    }
}
