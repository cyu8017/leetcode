<?php
// LeetCode 1274 - Number of Ships in a Rectangle
// https://leetcode.com/problems/number-of-ships-in-a-rectangle/

class Solution {
    /**
     * @param Sea $sea
     * @param Integer[] $topRight
     * @param Integer[] $bottomLeft
     * @return Integer
     */
    function countShips($sea, $topRight, $bottomLeft) {
        [$tx, $ty] = $topRight;
        [$bx, $by] = $bottomLeft;
        if ($tx < $bx || $ty < $by || !$sea->hasShips($topRight, $bottomLeft)) return 0;
        if ($tx === $bx && $ty === $by) return 1;
        $mx = intdiv($tx + $bx, 2);
        $my = intdiv($ty + $by, 2);
        return $this->countShips($sea, [$mx, $my], [$bx, $by])
            + $this->countShips($sea, [$tx, $my], [$mx + 1, $by])
            + $this->countShips($sea, [$mx, $ty], [$bx, $my + 1])
            + $this->countShips($sea, [$tx, $ty], [$mx + 1, $my + 1]);
    }
}
