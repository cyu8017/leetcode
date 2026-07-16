<?php
// LeetCode 0492 - Construct the Rectangle
// https://leetcode.com/problems/construct-the-rectangle/

class Solution {
    /**
     * @param Integer $area
     * @return Integer[]
     */
    function constructRectangle($area) {
        return $this->construct_rectangle($area);
    }

    /**
     * @param Integer $area
     * @return Integer[]
     */
    function construct_rectangle($area) {
        $width = (int) floor(sqrt($area));
        while ($width > 0) {
            if ($area % $width === 0) {
                return [$area / $width, $width];
            }
            $width--;
        }
        return [$area, 1];
    }
}
