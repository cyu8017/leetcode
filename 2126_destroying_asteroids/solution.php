<?php
// LeetCode 2126 - Destroying Asteroids
// https://leetcode.com/problems/destroying-asteroids/

class Solution {
    /**
     * @param Integer $mass
     * @param Integer[] $asteroids
     * @return Boolean
     */
    function asteroidsDestroyed($mass, $asteroids) {
        sort($asteroids);
        $cur = $mass;
        foreach ($asteroids as $a) {
            if ($cur < $a) return false;
            $cur += $a;
        }
        return true;
    }
}
