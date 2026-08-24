<?php
// LeetCode 2775 - Undefined to Null
// https://leetcode.com/problems/undefined-to-null/

class Solution {
    function undefinedToNull($obj) {
        if ($obj === null) return null;
        if (!is_array($obj) && !is_object($obj)) return $obj;
        if (is_object($obj)) $obj = (array)$obj;
        $isList = $obj === [] || array_keys($obj) === range(0, count($obj) - 1);
        if ($isList) {
            foreach ($obj as $i => $v) $obj[$i] = $this->undefinedToNull($v);
            return $obj;
        }
        foreach ($obj as $k => $v) $obj[$k] = $this->undefinedToNull($v);
        return $obj;
    }
}
