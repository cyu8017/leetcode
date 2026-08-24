<?php
// LeetCode 3481 - Apply Substitutions
// https://leetcode.com/problems/apply-substitutions/

class Solution {
    function applySubstitutions($replacements, $text) {
        $mp = [];
        foreach ($replacements as $r) $mp[$r[0]] = $r[1];
        $resolve = null;
        $resolve = function($s) use (&$resolve, &$mp) {
            $out = "";
            $n = strlen($s);
            for ($i = 0; $i < $n; ) {
                if ($s[$i] === "%") {
                    $j = $i + 1;
                    while ($j < $n && $s[$j] !== "%") $j++;
                    $key = substr($s, $i + 1, $j - ($i + 1));
                    $out .= $resolve($mp[$key]);
                    $i = $j + 1;
                } else {
                    $out .= $s[$i];
                    $i++;
                }
            }
            return $out;
        };
        return $resolve($text);
    }
}
