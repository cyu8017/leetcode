<?php
// LeetCode 0179 - Largest Number
// https://leetcode.com/problems/largest-number/

class Solution {
    function largestNumber(array $nums): string {
        $parts = array_map("strval", $nums);
        usort($parts, function (string $left, string $right): int {
            return strcmp($right . $left, $left . $right);
        });
        return $parts[0] === "0" ? "0" : implode("", $parts);
    }
}
