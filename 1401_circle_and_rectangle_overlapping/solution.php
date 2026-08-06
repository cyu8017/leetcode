<?php
class Solution {
    function checkOverlap($radius, $xCenter, $yCenter, $x1, $y1, $x2, $y2) {
        $x = min(max($xCenter, $x1), $x2);
        $y = min(max($yCenter, $y1), $y2);
        return ($x - $xCenter) ** 2 + ($y - $yCenter) ** 2 <= $radius ** 2;
    }
}
