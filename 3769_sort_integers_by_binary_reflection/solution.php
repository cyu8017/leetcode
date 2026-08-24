<?php
// LeetCode 3769 - Sort Integers by Binary Reflection
// https://leetcode.com/problems/sort-integers-by-binary-reflection/

class Solution {
    function sortByReflection($nums) {
        $f = function($x) {
            $y = 0;
            while ($x !== 0) {
                $y = ($y << 1) | ($x & 1);
                $x >>= 1;
            }
            return $y;
        };
        $arr = $nums;
        usort($arr, function($a, $b) use ($f) {
            $fa = $f($a);
            $fb = $f($b);
            if ($fa !== $fb) return $fa <=> $fb;
            return $a <=> $b;
        });
        for ($i = 0; $i < count($nums); $i++) $nums[$i] = $arr[$i];
        return $nums;
    }
}
