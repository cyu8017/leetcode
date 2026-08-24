<?php
// LeetCode 2794 - Create Object from Two Arrays
// https://leetcode.com/problems/create-object-from-two-arrays/

class Solution {
    function createObject($keysArr, $valuesArr) {
        $output = [];
        $n = min(count($keysArr), count($valuesArr));
        for ($i = 0; $i < $n; $i++) {
            $k = is_bool($keysArr[$i]) ? ($keysArr[$i] ? 'true' : 'false') : (string)$keysArr[$i];
            if (!array_key_exists($k, $output)) $output[$k] = $valuesArr[$i];
        }
        return $output;
    }
}
