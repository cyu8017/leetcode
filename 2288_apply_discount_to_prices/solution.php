<?php
// LeetCode 2288 - Apply Discount to Prices
// https://leetcode.com/problems/apply-discount-to-prices/

class Solution {
    function discountPrices($sentence, $discount) {
        $parts = explode(' ', $sentence);
        for ($i = 0; $i < count($parts); $i++) {
            $part = $parts[$i];
            if (strlen($part) >= 2 && $part[0] === '$') {
                $ok = true;
                $pn = strlen($part);
                for ($j = 1; $j < $pn; $j++) {
                    if ($part[$j] < '0' || $part[$j] > '9') { $ok = false; break; }
                }
                if ($ok) {
                    $val = floatval(substr($part, 1));
                    $price = $val * (100 - $discount) / 100.0;
                    $parts[$i] = '$' . number_format($price, 2, '.', '');
                }
            }
        }
        return implode(' ', $parts);
    }
}
