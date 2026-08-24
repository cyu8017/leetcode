<?php
// LeetCode 0575 - Distribute Candies
// https://leetcode.com/problems/distribute-candies/

class Solution {
    function distributeCandies($candyType) {
        return min(count(array_unique($candyType)), intdiv(count($candyType), 2));
    }
}
