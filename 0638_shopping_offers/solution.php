<?php
// LeetCode 0638 - Shopping Offers
// https://leetcode.com/problems/shopping-offers/

class Solution {
    function shoppingOffers($price, $special, $needs) {
        $memo = [];
        $dfs = function($state) use (&$dfs, &$memo, $price, $special) {
            $key = implode(",", $state);
            if (isset($memo[$key])) return $memo[$key];
            $cost = 0;
            for ($i = 0; $i < count($price); ++$i) $cost += $state[$i] * $price[$i];
            foreach ($special as $offer) {
                $nxt = $state;
                $valid = true;
                for ($i = 0; $i < count($price); ++$i) {
                    if ($nxt[$i] < $offer[$i]) { $valid = false; break; }
                    $nxt[$i] -= $offer[$i];
                }
                if ($valid) $cost = min($cost, $offer[count($price)] + $dfs($nxt));
            }
            $memo[$key] = $cost;
            return $cost;
        };
        return $dfs($needs);
    }
}
