<?php
// LeetCode 1103 - Distribute Candies to People
// https://leetcode.com/problems/distribute-candies-to-people/

class Solution {
    /**
     * @param Integer $candies
     * @param Integer $num_people
     * @return Integer[]
     */
    function distributeCandies($candies, $num_people) {
        $ans = array_fill(0, $num_people, 0);
        $give = 1;
        $i = 0;
        while ($candies > 0) {
            $take = min($give, $candies);
            $ans[$i] += $take;
            $candies -= $take;
            $give++;
            $i = ($i + 1) % $num_people;
        }
        return $ans;
    }
}
