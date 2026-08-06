<?php
class Solution {
    function filterRestaurants($restaurants, $veganFriendly, $maxPrice, $maxDistance) {
        $valid = [];
        foreach ($restaurants as $row) {
            if ((!$veganFriendly || $row[2]) && $row[3] <= $maxPrice && $row[4] <= $maxDistance) {
                $valid[] = $row;
            }
        }
        usort($valid, function($a, $b) {
            if ($a[1] !== $b[1]) return $b[1] <=> $a[1];
            return $b[0] <=> $a[0];
        });
        $answer = [];
        foreach ($valid as $row) $answer[] = $row[0];
        return $answer;
    }
}
