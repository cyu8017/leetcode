<?php
// LeetCode 0741 - Cherry Pickup
// https://leetcode.com/problems/cherry-pickup/

class Solution {
    function cherryPickup($grid) {
        $n = count($grid);
        $UNSET = -INF;
        $memo = array_fill(0, $n, array_fill(0, $n, array_fill(0, $n, $UNSET)));
        $dp = function ($r1, $c1, $c2) use (&$dp, &$memo, &$grid, $n, $UNSET) {
            $r2 = $r1 + $c1 - $c2;
            if ($r1 >= $n || $c1 >= $n || $r2 >= $n || $c2 >= $n || $grid[$r1][$c1] === -1 || $grid[$r2][$c2] === -1)
                return -1000000000;
            if ($r1 === $n - 1 && $c1 === $n - 1) return $grid[$r1][$c1];
            if ($memo[$r1][$c1][$c2] !== $UNSET) return $memo[$r1][$c1][$c2];
            $cherries = $grid[$r1][$c1];
            if ($r1 !== $r2 || $c1 !== $c2) $cherries += $grid[$r2][$c2];
            $cherries += max(
                max($dp($r1 + 1, $c1, $c2), $dp($r1, $c1 + 1, $c2)),
                max($dp($r1 + 1, $c1, $c2 + 1), $dp($r1, $c1 + 1, $c2 + 1))
            );
            $memo[$r1][$c1][$c2] = $cherries;
            return $cherries;
        };
        return max(0, $dp(0, 0, 0));
    }
}
