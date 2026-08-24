<?php
// LeetCode 0806 - Number of Lines To Write String
// https://leetcode.com/problems/number-of-lines-to-write-string/

class Solution {
    /**
     * @param Integer[] $widths
     * @param String $s
     * @return Integer[]
     */
    function numberOfLines($widths, $s) {
        $lines = 1;
        $width = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $w = $widths[ord($s[$i]) - 97];
            if ($width + $w > 100) {
                $lines++;
                $width = $w;
            } else {
                $width += $w;
            }
        }
        return [$lines, $width];
    }
}
