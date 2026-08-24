<?php
// LeetCode 2079 - Watering Plants
// https://leetcode.com/problems/watering-plants/

class Solution {
    /**
     * @param Integer[] $plants
     * @param Integer $capacity
     * @return Integer
     */
    function wateringPlants($plants, $capacity) {
        $ans = 0;
        $cur = $capacity;
        $n = count($plants);
        for ($i = 0; $i < $n; $i++) {
            if ($cur < $plants[$i]) { $ans += $i * 2; $cur = $capacity; }
            $cur -= $plants[$i];
            $ans++;
        }
        return $ans;
    }
}
