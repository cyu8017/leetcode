<?php
// LeetCode 0478 - Generate Random Point in a Circle
// https://leetcode.com/problems/generate-random-point-in-a-circle/

$uniform = null;

function set_uniform($fn) {
    global $uniform;
    $uniform = $fn;
}

class Solution {
    private float $radius;
    private float $xCenter;
    private float $yCenter;

    function __construct(float $radius, float $xCenter, float $yCenter) {
        $this->radius = $radius;
        $this->xCenter = $xCenter;
        $this->yCenter = $yCenter;
    }

    /**
     * @return float[]
     */
    function randPoint() {
        global $uniform;
        while (true) {
            $x = $uniform(-$this->radius, $this->radius);
            $y = $uniform(-$this->radius, $this->radius);
            if ($x * $x + $y * $y <= $this->radius * $this->radius) {
                return [
                    round($this->xCenter + $x, 5),
                    round($this->yCenter + $y, 5),
                ];
            }
        }
    }
}
