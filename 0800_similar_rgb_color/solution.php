<?php
// LeetCode 0800 - Similar RGB Color
// https://leetcode.com/problems/similar-rgb-color/

class Solution {
    /**
     * @param String $color
     * @return String
     */
    function similarRGB($color) {
        $closest = function($component) {
            $value = hexdec($component);
            $rounded = intdiv($value + 8, 17);
            $hex = dechex($rounded);
            return $hex . $hex;
        };
        return "#" . $closest(substr($color, 1, 2)) . $closest(substr($color, 3, 2)) . $closest(substr($color, 5, 2));
    }
}
