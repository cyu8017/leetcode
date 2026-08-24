<?php
// LeetCode 2013 - Detect Squares
// https://leetcode.com/problems/detect-squares/

class DetectSquares {
    private $cnt = [];

    function __construct() {
        $this->cnt = [];
    }

    private function key($x, $y) {
        return $x . "," . $y;
    }

    /**
     * @param Integer[] $point
     * @return NULL
     */
    function add($point) {
        $k = $this->key($point[0], $point[1]);
        $this->cnt[$k] = ($this->cnt[$k] ?? 0) + 1;
    }

    /**
     * @param Integer[] $point
     * @return Integer
     */
    function count($point) {
        $x = $point[0];
        $y = $point[1];
        $ans = 0;
        foreach ($this->cnt as $k => $c) {
            [$px, $py] = array_map('intval', explode(",", $k));
            if ($px === $x || $py === $y) continue;
            if (abs($px - $x) !== abs($py - $y)) continue;
            $c1 = $this->cnt[$this->key($px, $y)] ?? 0;
            $c2 = $this->cnt[$this->key($x, $py)] ?? 0;
            $ans += $c * $c1 * $c2;
        }
        return $ans;
    }
}
