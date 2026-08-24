<?php
// LeetCode 2438 - Range Product Queries of Powers
// https://leetcode.com/problems/range-product-queries-of-powers/

class Solution {
    function productQueries($n, $queries) {
        $mod = 1000000007;
        $powers = [];
        for ($bit = 0; $bit < 31; $bit++) {
            if ((($n >> $bit) & 1) !== 0) $powers[] = 1 << $bit;
        }
        $ans = array_fill(0, count($queries), 0);
        for ($i = 0; $i < count($queries); $i++) {
            $prod = 1;
            for ($j = $queries[$i][0]; $j <= $queries[$i][1]; $j++)
                $prod = ($prod * $powers[$j]) % $mod;
            $ans[$i] = $prod;
        }
        return $ans;
    }
}
