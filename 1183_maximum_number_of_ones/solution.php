<?php
// LeetCode 1183 - Maximum Number of Ones
// https://leetcode.com/problems/maximum-number-of-ones/

class Solution {
    /**
     * @param Integer $width
     * @param Integer $height
     * @param Integer $sideLength
     * @param Integer $maxOnes
     * @return Integer
     */
    function maximumNumberOfOnes($width, $height, $sideLength, $maxOnes) {
        $counts = [];
        for ($r = 0; $r < $sideLength; $r++) {
            for ($c = 0; $c < $sideLength; $c++) {
                $rows = intdiv($height - $r + $sideLength - 1, $sideLength);
                $cols = intdiv($width - $c + $sideLength - 1, $sideLength);
                $counts[] = $rows * $cols;
            }
        }
        rsort($counts);
        return array_sum(array_slice($counts, 0, $maxOnes));
    }
}
