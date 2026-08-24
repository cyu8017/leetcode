<?php
// LeetCode 0957 - Prison Cells After N Days
// https://leetcode.com/problems/prison-cells-after-n-days/

class Solution {
    function prisonAfterNDays($cells, $n) {
        $seen = [];
        $state = $cells;
        while ($n > 0) {
            $key = implode(",", $state);
            if (isset($seen[$key])) {
                $cycle = $seen[$key] - $n;
                $n %= $cycle;
                if ($n === 0) break;
            }
            $seen[$key] = $n;
            $nxt = array_fill(0, 8, 0);
            for ($i = 1; $i <= 6; $i++) $nxt[$i] = $state[$i - 1] === $state[$i + 1] ? 1 : 0;
            $state = $nxt;
            $n--;
        }
        return $state;
    }
}
