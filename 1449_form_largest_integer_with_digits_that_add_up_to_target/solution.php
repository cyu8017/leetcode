<?php
class Solution {
    function largestNumber($cost, $target) {
        $dp = array_fill(0, $target + 1, null);
        $dp[0] = "";
        for ($total = 1; $total <= $target; $total++) {
            $best = null;
            for ($digit = 1; $digit <= 9; $digit++) {
                $price = $cost[$digit - 1];
                if ($total >= $price && $dp[$total - $price] !== null) {
                    $candidate = strval($digit) . $dp[$total - $price];
                    if ($best === null || strlen($candidate) > strlen($best) || (strlen($candidate) === strlen($best) && $candidate > $best)) {
                        $best = $candidate;
                    }
                }
            }
            $dp[$total] = $best;
        }
        return $dp[$target] ?? "0";
    }
}
