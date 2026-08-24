<?php
// LeetCode 2878 - Get the Size of a DataFrame
// https://leetcode.com/problems/get-the-size-of-a-dataframe/

class Solution {
    function getDataframeSize($players) {
        if (!$players || count($players) === 0) return [0, 0];
        $rows = count($players);
        $first = $players[0];
        $cols = (is_array($first) && array_keys($first) === range(0, count($first) - 1))
            ? count($first)
            : count((array)$first);
        return [$rows, $cols];
    }
}
