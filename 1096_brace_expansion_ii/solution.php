<?php
// LeetCode 1096 - Brace Expansion II
// https://leetcode.com/problems/brace-expansion-ii/

class Solution {
    /**
     * @param String $expression
     * @return String[]
     */
    function braceExpansionII($expression) {
        $parse = null;
        $parse = function ($expr, $i) use (&$parse) {
            $union = [];
            $cur = ["" => true];
            $len = strlen($expr);
            while ($i < $len && $expr[$i] !== "}") {
                if ($expr[$i] === "{") {
                    [$nested, $i] = $parse($expr, $i + 1);
                    $next = [];
                    foreach ($cur as $a => $_) {
                        foreach ($nested as $b => $__) {
                            $next[$a . $b] = true;
                        }
                    }
                    $cur = $next;
                } elseif ($expr[$i] === ",") {
                    foreach ($cur as $a => $_) {
                        $union[$a] = true;
                    }
                    $cur = ["" => true];
                    $i++;
                } else {
                    $j = $i;
                    while ($j < $len && ctype_alpha($expr[$j])) {
                        $j++;
                    }
                    $token = substr($expr, $i, $j - $i);
                    $next = [];
                    foreach ($cur as $a => $_) {
                        $next[$a . $token] = true;
                    }
                    $cur = $next;
                    $i = $j;
                }
            }
            foreach ($cur as $a => $_) {
                $union[$a] = true;
            }
            return [$union, $i + 1];
        };
        [$result] = $parse($expression, 0);
        $ans = array_keys($result);
        sort($ans);
        return $ans;
    }
}
