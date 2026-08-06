<?php
class Solution {
    function kidsWithCandies($candies, $extraCandies) {
        $maximum = max($candies);
        $answer = [];
        foreach ($candies as $value) $answer[] = $value + $extraCandies >= $maximum;
        return $answer;
    }
}
