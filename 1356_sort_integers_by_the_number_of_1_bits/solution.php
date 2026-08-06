<?php
class Solution {
    function sortByBits($arr) {
        usort($arr, function($a, $b) {
            $ca = substr_count(decbin($a), "1");
            $cb = substr_count(decbin($b), "1");
            if ($ca !== $cb) return $ca <=> $cb;
            return $a <=> $b;
        });
        return $arr;
    }
}
