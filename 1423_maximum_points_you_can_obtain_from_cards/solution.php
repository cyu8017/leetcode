<?php
class Solution {
    function maxScore($cardPoints, $k) {
        $n = count($cardPoints);
        if ($k === $n) return array_sum($cardPoints);
        $window = $n - $k;
        $current = array_sum(array_slice($cardPoints, 0, $window));
        $smallest = $current;
        for ($i = $window; $i < $n; $i++) {
            $current += $cardPoints[$i] - $cardPoints[$i - $window];
            $smallest = min($smallest, $current);
        }
        return array_sum($cardPoints) - $smallest;
    }
}
