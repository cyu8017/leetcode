<?php
// LeetCode 2353 - Design a Food Rating System
// https://leetcode.com/problems/design-a-food-rating-system/

class FoodRatings {
    private $cuisineOf;
    private $ratingOf;
    private $heaps;

    function __construct($foods, $cuisines, $ratings) {
        $this->cuisineOf = [];
        $this->ratingOf = [];
        $this->heaps = [];
        $n = count($foods);
        for ($i = 0; $i < $n; $i++) {
            $this->cuisineOf[$foods[$i]] = $cuisines[$i];
            $this->ratingOf[$foods[$i]] = $ratings[$i];
            if (!isset($this->heaps[$cuisines[$i]])) $this->heaps[$cuisines[$i]] = [];
            $this->heaps[$cuisines[$i]][] = $foods[$i];
        }
    }

    function changeRating($food, $newRating) {
        $this->ratingOf[$food] = $newRating;
    }

    function highestRated($cuisine) {
        $set = $this->heaps[$cuisine];
        $ratingOf = $this->ratingOf;
        usort($set, function($a, $b) use ($ratingOf) {
            $ra = $ratingOf[$a];
            $rb = $ratingOf[$b];
            if ($ra !== $rb) return $rb - $ra;
            return $a === $b ? 0 : ($a < $b ? -1 : 1);
        });
        return $set[0];
    }
}
