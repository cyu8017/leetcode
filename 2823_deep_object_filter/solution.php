<?php
// LeetCode 2823 - Deep Object Filter
// https://leetcode.com/problems/deep-object-filter/

class Solution {
    function deepFilter($obj, $fn) {
        if (!is_array($obj) && !is_object($obj)) {
            return $fn($obj) ? $obj : null;
        }
        if (is_object($obj)) $obj = (array)$obj;
        $isList = $obj === [] || array_keys($obj) === range(0, count($obj) - 1);
        if ($isList) {
            $res = [];
            foreach ($obj as $v) {
                $f = $this->deepFilter($v, $fn);
                if ($f !== null) $res[] = $f;
            }
            return $res ? $res : null;
        }
        $res = [];
        foreach ($obj as $k => $v) {
            $f = $this->deepFilter($v, $fn);
            if ($f !== null) $res[$k] = $f;
        }
        return $res ? $res : null;
    }
}
