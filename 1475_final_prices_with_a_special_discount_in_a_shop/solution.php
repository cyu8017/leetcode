<?php
class Solution {
    function finalPrices($prices) {
        $ans = $prices;
        $stack = [];
        foreach ($prices as $i => $price) {
            while ($stack && $prices[$stack[count($stack) - 1]] >= $price) {
                $j = array_pop($stack);
                $ans[$j] -= $price;
            }
            $stack[] = $i;
        }
        return $ans;
    }
}
