<?php
// LeetCode 2105 - Watering Plants II
// https://leetcode.com/problems/watering-plants-ii/

class Solution {
    /**
     * @param Integer[] $plants
     * @param Integer $capacityA
     * @param Integer $capacityB
     * @return Integer
     */
    function minimumRefill($plants, $capacityA, $capacityB) {
        $i = 0;
        $j = count($plants) - 1;
        $a = $capacityA;
        $b = $capacityB;
        $ans = 0;
        while ($i < $j) {
            if ($a < $plants[$i]) {
                $ans++;
                $a = $capacityA;
            }
            $a -= $plants[$i++];
            if ($b < $plants[$j]) {
                $ans++;
                $b = $capacityB;
            }
            $b -= $plants[$j--];
        }
        if ($i === $j) {
            if ($a >= $b) {
                if ($a < $plants[$i]) $ans++;
            } else if ($b < $plants[$i]) $ans++;
        }
        return $ans;
    }
}
