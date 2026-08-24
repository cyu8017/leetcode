<?php
// LeetCode 0554 - Brick Wall
// https://leetcode.com/problems/brick-wall/

class Solution {
    function leastBricks($wall) {
        $edges = [];
        $best = 0;
        foreach ($wall as $row) {
            $width = 0;
            for ($i = 0; $i + 1 < count($row); ++$i) {
                $width += $row[$i];
                $count = ($edges[$width] ?? 0) + 1;
                $edges[$width] = $count;
                $best = max($best, $count);
            }
        }
        return count($wall) - $best;
    }
}
