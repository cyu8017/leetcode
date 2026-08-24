<?php
// LeetCode 2782 - Number of Unique Categories
// https://leetcode.com/problems/number-of-unique-categories/

class CategoryHandler {
    public $cats;
    function __construct($cats) {
        $this->cats = $cats;
    }
    function haveSameCategory($a, $b) {
        return $this->cats[$a] === $this->cats[$b];
    }
}

class Solution {
    function numberOfCategories($n, $categoryHandler) {
        if (is_array($categoryHandler)) $categoryHandler = new CategoryHandler($categoryHandler);
        $parent = range(0, $n - 1);
        $find = function($x) use (&$parent, &$find) {
            while ($parent[$x] !== $x) {
                $parent[$x] = $parent[$parent[$x]];
                $x = $parent[$x];
            }
            return $x;
        };
        for ($i = 0; $i < $n; $i++) {
            for ($j = $i + 1; $j < $n; $j++) {
                if ($categoryHandler->haveSameCategory($i, $j)) {
                    $a = $find($i);
                    $b = $find($j);
                    if ($a !== $b) $parent[$a] = $b;
                }
            }
        }
        $ans = 0;
        for ($i = 0; $i < $n; $i++) if ($find($i) === $i) $ans++;
        return $ans;
    }
}
