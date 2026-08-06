<?php
// LeetCode 1104 - Path In Zigzag Labelled Binary Tree
// https://leetcode.com/problems/path-in-zigzag-labelled-binary-tree/

class Solution {
    /**
     * @param Integer $label
     * @return Integer[]
     */
    function pathInZigZagTree($label) {
        $path = [$label];
        while ($label > 1) {
            $level = (int)floor(log($label, 2));
            $label >>= 1;
            $label = (1 << $level) - 1 - $label + (1 << ($level - 1));
            $path[] = $label;
        }
        return array_reverse($path);
    }
}
