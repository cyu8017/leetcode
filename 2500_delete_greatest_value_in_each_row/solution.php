<?php
// LeetCode 2500 - Delete Greatest Value in Each Row
// https://leetcode.com/problems/delete-greatest-value-in-each-row/

class Solution {
    function deleteGreatestValue($grid) {
        foreach ($grid as &$row) sort($row);
        unset($row);
        $ans = 0;
        $n = count($grid[0]);
        for ($c = 0; $c < $n; $c++) {
            $mx = 0;
            foreach ($grid as $row) if ($row[$c] > $mx) $mx = $row[$c];
            $ans += $mx;
        }
        return $ans;
    }
}
