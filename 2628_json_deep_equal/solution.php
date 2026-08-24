<?php
// LeetCode 2628 - JSON Deep Equal
// https://leetcode.com/problems/json-deep-equal/

class Solution {
    function areDeeplyEqual($o1, $o2) {
        if ($o1 === $o2) return true;
        if (gettype($o1) !== gettype($o2)) return false;
        if ($o1 === null || $o2 === null) return false;
        if (!is_array($o1)) return false;
        $a1 = array_is_list($o1);
        $a2 = array_is_list($o2);
        if ($a1 !== $a2) return false;
        if ($a1) {
            if (count($o1) !== count($o2)) return false;
            for ($i = 0; $i < count($o1); $i++) {
                if (!$this->areDeeplyEqual($o1[$i], $o2[$i])) return false;
            }
            return true;
        }
        $k1 = array_keys($o1);
        $k2 = array_keys($o2);
        if (count($k1) !== count($k2)) return false;
        foreach ($k1 as $k) {
            if (!array_key_exists($k, $o2) || !$this->areDeeplyEqual($o1[$k], $o2[$k])) return false;
        }
        return true;
    }
}
