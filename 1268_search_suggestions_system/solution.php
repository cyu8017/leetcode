<?php
// LeetCode 1268 - Search Suggestions System
// https://leetcode.com/problems/search-suggestions-system/

class Solution {
    /**
     * @param String[] $products
     * @param String $searchWord
     * @return String[][]
     */
    function suggestedProducts($products, $searchWord) {
        sort($products);
        $answer = [];
        $prefix = '';
        $len = strlen($searchWord);
        for ($i = 0; $i < $len; $i++) {
            $prefix .= $searchWord[$i];
            $lo = 0; $hi = count($products);
            while ($lo < $hi) {
                $mid = ($lo + $hi) >> 1;
                if ($products[$mid] < $prefix) $lo = $mid + 1;
                else $hi = $mid;
            }
            $group = [];
            for ($j = $lo; $j < min($lo + 3, count($products)); $j++) {
                if (str_starts_with($products[$j], $prefix)) $group[] = $products[$j];
            }
            $answer[] = $group;
        }
        return $answer;
    }
}
