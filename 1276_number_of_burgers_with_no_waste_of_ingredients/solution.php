<?php
// LeetCode 1276 - Number of Burgers with No Waste of Ingredients
// https://leetcode.com/problems/number-of-burgers-with-no-waste-of-ingredients/

class Solution {
    /**
     * @param Integer $tomatoSlices
     * @param Integer $cheeseSlices
     * @return Integer[]
     */
    function numOfBurgers($tomatoSlices, $cheeseSlices) {
        if ($tomatoSlices % 2 !== 0) return [];
        $jumbo = intdiv($tomatoSlices, 2) - $cheeseSlices;
        $small = $cheeseSlices - $jumbo;
        return ($jumbo >= 0 && $small >= 0) ? [$jumbo, $small] : [];
    }
}
