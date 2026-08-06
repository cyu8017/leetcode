<?php
class Solution {
    function getNoZeroIntegers($n) {
        $valid = function($value) {
            return strpos(strval($value), "0") === false;
        };
        for ($first = 1; $first < $n; $first++) {
            if ($valid($first) && $valid($n - $first)) return [$first, $n - $first];
        }
        return [];
    }
}
