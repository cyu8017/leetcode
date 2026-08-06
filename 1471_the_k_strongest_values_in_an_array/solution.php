<?php
class Solution {
    function getStrongest($arr, $k) {
        sort($arr);
        $median = $arr[intdiv(count($arr) - 1, 2)];
        usort($arr, function($a, $b) use ($median) {
            $da = abs($a - $median);
            $db = abs($b - $median);
            if ($da !== $db) return $db <=> $da;
            return $b <=> $a;
        });
        return array_slice($arr, 0, $k);
    }
}
