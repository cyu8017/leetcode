<?php
// LeetCode 2755 - Deep Merge of Two Objects
// https://leetcode.com/problems/deep-merge-of-two-objects/

class Solution {
    function deepMerge($obj1, $obj2) {
        $isList = function($x) {
            if (!is_array($x)) return false;
            if ($x === []) return true;
            return array_keys($x) === range(0, count($x) - 1);
        };
        $isObj = function($x) use ($isList) {
            return is_array($x) && !$isList($x) || is_object($x);
        };
        if ($isObj($obj1) && $isObj($obj2)) {
            $a = (array)$obj1;
            $b = (array)$obj2;
            $res = $a;
            foreach ($b as $k => $v) {
                if (array_key_exists($k, $res)) $res[$k] = $this->deepMerge($res[$k], $v);
                else $res[$k] = $v;
            }
            return $res;
        }
        if ($isList($obj1) && $isList($obj2)) {
            $n = max(count($obj1), count($obj2));
            $res = [];
            for ($i = 0; $i < $n; $i++) {
                if ($i >= count($obj1)) $res[$i] = $obj2[$i];
                else if ($i >= count($obj2)) $res[$i] = $obj1[$i];
                else $res[$i] = $this->deepMerge($obj1[$i], $obj2[$i]);
            }
            return $res;
        }
        return $obj2;
    }
}
