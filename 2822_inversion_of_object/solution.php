<?php
// LeetCode 2822 - Inversion of Object
// https://leetcode.com/problems/inversion-of-object/

class Solution {
    function invertObject($obj) {
        $inverted = [];
        if (is_object($obj)) $obj = (array)$obj;
        foreach ($obj as $key => $val) {
            $val = is_bool($val) ? ($val ? 'true' : 'false') : (string)$val;
            $key = (string)$key;
            if (array_key_exists($val, $inverted)) {
                if (!is_array($inverted[$val])) $inverted[$val] = [$inverted[$val]];
                $inverted[$val][] = $key;
            } else {
                $inverted[$val] = $key;
            }
        }
        return $inverted;
    }
}
