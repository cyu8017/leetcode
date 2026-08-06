<?php
class Solution {
    function canReach($arr, $start) {
        $stack = [$start];
        $seen = [];
        while ($stack) {
            $i = array_pop($stack);
            if (isset($seen[$i]) || $i < 0 || $i >= count($arr)) continue;
            if ($arr[$i] === 0) return true;
            $seen[$i] = true;
            $stack[] = $i - $arr[$i];
            $stack[] = $i + $arr[$i];
        }
        return false;
    }
}
