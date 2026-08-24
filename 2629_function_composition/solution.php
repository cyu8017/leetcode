<?php
// LeetCode 2629 - Function Composition
// https://leetcode.com/problems/function-composition/

class Solution {
    function compose($functions) {
        return function($x) use ($functions) {
            for ($i = count($functions) - 1; $i >= 0; $i--) $x = $functions[$i]($x);
            return $x;
        };
    }
}
