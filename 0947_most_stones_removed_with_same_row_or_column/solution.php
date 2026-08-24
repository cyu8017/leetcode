<?php
// LeetCode 0947 - Most Stones Removed with Same Row or Column
// https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

class Solution {
    function removeStones($stones) {
        $parent = [];
        $find = function ($x) use (&$find, &$parent) {
            if (!array_key_exists($x, $parent)) $parent[$x] = $x;
            if ($parent[$x] !== $x) $parent[$x] = $find($parent[$x]);
            return $parent[$x];
        };
        foreach ($stones as $s) {
            $parent[$find($s[0])] = $find(~$s[1]);
        }
        $roots = [];
        foreach ($stones as $s) $roots[$find($s[0])] = true;
        return count($stones) - count($roots);
    }
}
