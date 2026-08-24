<?php
// LeetCode 0839 - Similar String Groups
// https://leetcode.com/problems/similar-string-groups/

class Solution {
    /**
     * @param String[] $strs
     * @return Integer
     */
    function numSimilarGroups($strs) {
        $n = count($strs);
        $parent = range(0, $n - 1);
        $find = function($x) use (&$parent) {
            while ($parent[$x] !== $x) {
                $parent[$x] = $parent[$parent[$x]];
                $x = $parent[$x];
            }
            return $x;
        };
        $similar = function($a, $b) {
            $d0 = -1;
            $d1 = -1;
            $diffs = 0;
            $len = strlen($a);
            for ($i = 0; $i < $len; $i++) {
                if ($a[$i] !== $b[$i]) {
                    $diffs++;
                    if ($diffs > 2) return false;
                    if ($d0 < 0) $d0 = $i;
                    else $d1 = $i;
                }
            }
            return $diffs === 0 || ($diffs === 2 && $a[$d0] === $b[$d1] && $a[$d1] === $b[$d0]);
        };
        $groups = $n;
        for ($i = 0; $i < $n; $i++) {
            for ($j = $i + 1; $j < $n; $j++) {
                if ($similar($strs[$i], $strs[$j])) {
                    $pi = $find($i);
                    $pj = $find($j);
                    if ($pi !== $pj) {
                        $parent[$pi] = $pj;
                        $groups--;
                    }
                }
            }
        }
        return $groups;
    }
}
