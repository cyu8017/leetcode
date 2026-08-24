<?php
// LeetCode 0391 - Perfect Rectangle
// https://leetcode.com/problems/perfect-rectangle/

class Solution {
    /**
     * @param Integer[][] $rectangles
     * @return Boolean
     */
    function isRectangleCover($rectangles) {
        return $this->is_rectangle_cover($rectangles);
    }

    /**
     * @param Integer[][] $rectangles
     * @return Boolean
     */
    function is_rectangle_cover($rectangles) {
        $points = [];
        $area = 0;
        $minX = PHP_INT_MAX;
        $minY = PHP_INT_MAX;
        $maxX = PHP_INT_MIN;
        $maxY = PHP_INT_MIN;

        foreach ($rectangles as $rectangle) {
            [$x1, $y1, $x2, $y2] = $rectangle;
            $area += ($x2 - $x1) * ($y2 - $y1);
            $minX = min($minX, $x1);
            $minY = min($minY, $y1);
            $maxX = max($maxX, $x2);
            $maxY = max($maxY, $y2);

            foreach ([[$x1, $y1], [$x1, $y2], [$x2, $y1], [$x2, $y2]] as $point) {
                $key = $point[0] . "," . $point[1];
                if (isset($points[$key])) {
                    unset($points[$key]);
                } else {
                    $points[$key] = true;
                }
            }
        }

        $corners = [
            $minX . "," . $minY,
            $minX . "," . $maxY,
            $maxX . "," . $minY,
            $maxX . "," . $maxY,
        ];
        if (count($points) !== 4) {
            return false;
        }
        foreach ($corners as $corner) {
            if (!isset($points[$corner])) {
                return false;
            }
        }

        return $area === ($maxX - $minX) * ($maxY - $minY);
    }
}
