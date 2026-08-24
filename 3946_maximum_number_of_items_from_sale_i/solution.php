<?php
// LeetCode 3946 - Maximum Number Of Items From Sale I
// https://leetcode.com/problems/maximum-number-of-items-from-sale-i/

class Solution {
    function maximumSaleItems($items, $budget) {
        $f = array_fill(0, $budget + 1, 0);
        $mn = 2147483647;
        foreach ($items as $item) {
            $factor = $item[0];
            $price = $item[1];
            $mn = min($mn, $price);
            $cnt = 0;
            foreach ($items as $jItem) {
                if ($jItem[0] % $factor == 0) $cnt++;
            }
            for ($j = $budget; $j >= $price; $j--) {
                $f[$j] = max($f[$j], $f[$j - $price] + $cnt);
            }
        }
        $ans = 0;
        for ($i = 0; $i <= $budget; $i++) {
            $extra = intdiv($budget - $i, $mn);
            $ans = max($ans, $f[$i] + $extra);
        }
        return $ans;
    }
}
