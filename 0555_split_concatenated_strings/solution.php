<?php
// LeetCode 0555 - Split Concatenated Strings
// https://leetcode.com/problems/split-concatenated-strings/

class Solution {
    function splitLoopedString($strs) {
        $n = count($strs);
        $bestForms = array_fill(0, $n, "");
        for ($i = 0; $i < $n; ++$i) {
            $s = $strs[$i];
            $rev = strrev($s);
            $bestForms[$i] = $s >= $rev ? $s : $rev;
        }
        $answer = "";
        for ($i = 0; $i < $n; ++$i) {
            $mid = "";
            for ($j = $i + 1; $j < $n; ++$j) $mid .= $bestForms[$j];
            for ($j = 0; $j < $i; ++$j) $mid .= $bestForms[$j];
            $candidates = [$strs[$i], strrev($strs[$i])];
            foreach ($candidates as $candidate) {
                $len = strlen($candidate);
                for ($cut = 0; $cut < $len; ++$cut) {
                    $formed = substr($candidate, $cut) . $mid . substr($candidate, 0, $cut);
                    if ($formed > $answer) $answer = $formed;
                }
            }
        }
        return $answer;
    }
}
