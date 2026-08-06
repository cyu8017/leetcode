<?php
// LeetCode 1202 - Smallest String With Swaps
// https://leetcode.com/problems/smallest-string-with-swaps/

class Solution {
    /**
     * @param String $s
     * @param Integer[][] $pairs
     * @return String
     */
    function smallestStringWithSwaps($s, $pairs) {
        $n = strlen($s);
        $parent = range(0, $n - 1);
        $find = function ($x) use (&$parent, &$find) {
            if ($parent[$x] !== $x) $parent[$x] = $find($parent[$x]);
            return $parent[$x];
        };
        foreach ($pairs as [$a, $b]) {
            $ra = $find($a); $rb = $find($b);
            if ($ra !== $rb) $parent[$rb] = $ra;
        }
        $groups = [];
        for ($i = 0; $i < $n; $i++) $groups[$find($i)][] = $i;
        $chars = str_split($s);
        foreach ($groups as $idxs) {
            $letters = [];
            foreach ($idxs as $i) $letters[] = $chars[$i];
            sort($letters);
            sort($idxs);
            foreach ($idxs as $j => $i) $chars[$i] = $letters[$j];
        }
        return implode('', $chars);
    }
}
