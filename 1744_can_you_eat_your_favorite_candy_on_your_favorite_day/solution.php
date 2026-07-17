<?php
// LeetCode 1744 - Can You Eat Your Favorite Candy on Your Favorite Day?
// https://leetcode.com/problems/can-you-eat-your-favorite-candy-on-your-favorite-day/

class Solution {
    /**
     * @param Integer[] $candiesCount
     * @param Integer[][] $queries
     * @return Boolean[]
     */
    function canEat($candiesCount, $queries) {
        $prefix = [0];
        foreach ($candiesCount as $count) {
            $prefix[] = $prefix[count($prefix) - 1] + $count;
        }
        $ans = [];
        foreach ($queries as [$candyType, $day, $cap]) {
            $minEaten = $day + 1;
            $maxEaten = ($day + 1) * $cap;
            $ans[] = $maxEaten > $prefix[$candyType] && $minEaten <= $prefix[$candyType + 1];
        }
        return $ans;
    }
}
