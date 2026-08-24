<?php
// LeetCode 0832 - Flipping an Image
// https://leetcode.com/problems/flipping-an-image/

class Solution {
    /**
     * @param Integer[][] $image
     * @return Integer[][]
     */
    function flipAndInvertImage($image) {
        foreach ($image as &$row) {
            $i = 0;
            $j = count($row) - 1;
            while ($i <= $j) {
                $a = 1 - $row[$i];
                $b = 1 - $row[$j];
                $row[$i] = $b;
                $row[$j] = $a;
                $i++;
                $j--;
            }
        }
        unset($row);
        return $image;
    }
}
