<?php
// LeetCode 3477 - Fruits Into Baskets II
// https://leetcode.com/problems/fruits-into-baskets-ii/

class Solution {
    function numOfUnplacedFruits($fruits, $baskets) {
        $used = array_fill(0, count($baskets), false);
        $unplaced = 0;
        foreach ($fruits as $f) {
            $placed = false;
            for ($j = 0; $j < count($baskets); $j++) {
                if (!$used[$j] && $baskets[$j] >= $f) {
                    $used[$j] = true;
                    $placed = true;
                    break;
                }
            }
            if (!$placed) $unplaced++;
        }
        return $unplaced;
    }
}
