<?php
// LeetCode 0990 - Satisfiability of Equality Equations
// https://leetcode.com/problems/satisfiability-of-equality-equations/

class Solution {
    /**
     * @param String[] $equations
     * @return Boolean
     */
    function equationsPossible($equations) {
        $parent = range(0, 25);
        $find = null;
        $find = function ($x) use (&$parent, &$find) {
            if ($parent[$x] !== $x) $parent[$x] = $find($parent[$x]);
            return $parent[$x];
        };
        foreach ($equations as $eq) {
            if ($eq[1] === '=') $parent[$find(ord($eq[0]) - 97)] = $find(ord($eq[3]) - 97);
        }
        foreach ($equations as $eq) {
            if ($eq[1] === '!' && $find(ord($eq[0]) - 97) === $find(ord($eq[3]) - 97)) return false;
        }
        return true;
    }
}
