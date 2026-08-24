<?php
// LeetCode 2700 - Differences Between Two Objects
// https://leetcode.com/problems/differences-between-two-objects/

class Solution {
    function objDiff($obj1, $obj2) {
        $diff = [];
        foreach ($obj1 as $k => $v1) {
            if (!array_key_exists($k, $obj2)) continue;
            $v2 = $obj2[$k];
            $bothObj = is_array($v1) && $v1 !== null && is_array($v2) && $v2 !== null
                && !array_is_list($v1) && !array_is_list($v2);
            $bothArr = is_array($v1) && is_array($v2) && array_is_list($v1) && array_is_list($v2);
            if ($bothObj || $bothArr) {
                $child = $this->objDiff($v1, $v2);
                if (count($child) > 0) $diff[$k] = $child;
            } else if ($v1 !== $v2) {
                $diff[$k] = [$v1, $v2];
            }
        }
        return $diff;
    }
}
