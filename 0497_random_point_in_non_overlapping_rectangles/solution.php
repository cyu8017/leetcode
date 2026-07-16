<?php
// LeetCode 0497 - Random Point in Non-overlapping Rectangles
// https://leetcode.com/problems/random-point-in-non-overlapping-rectangles/

$uniform = null;

function set_uniform($fn) {
    global $uniform;
    $uniform = $fn;
}

class Solution {
    /** @var int[][] */
    private $rects;

    /** @var int */
    private $total;

    /**
     * @param int[][] $rects
     */
    function __construct($rects) {
        $this->rects = $rects;
        $this->total = 0;
        foreach ($rects as [$a, $b, $x, $y]) {
            $this->total += ($x - $a + 1) * ($y - $b + 1);
        }
    }

    /**
     * @return int[]
     */
    function pick() {
        global $uniform;
        $index = (int) $uniform(0, $this->total);
        if ($index >= $this->total) {
            $index = $this->total - 1;
        }
        foreach ($this->rects as [$a, $b, $x, $y]) {
            $width = $x - $a + 1;
            $height = $y - $b + 1;
            $size = $width * $height;
            if ($index < $size) {
                $offsetX = $index % $width;
                $offsetY = intdiv($index, $width);
                return [$a + $offsetX, $b + $offsetY];
            }
            $index -= $size;
        }
        $last = $this->rects[count($this->rects) - 1];
        return [$last[0], $last[1]];
    }
}
