<?php
// LeetCode 2766 - Relocate Marbles
// https://leetcode.com/problems/relocate-marbles/

class Solution {
    function relocateMarbles($nums, $moveFrom, $moveTo) {
        $pos = array_fill_keys($nums, true);
        for ($i = 0; $i < count($moveFrom); $i++) {
            unset($pos[$moveFrom[$i]]);
            $pos[$moveTo[$i]] = true;
        }
        $keys = array_map('intval', array_keys($pos));
        sort($keys);
        return $keys;
    }
}
