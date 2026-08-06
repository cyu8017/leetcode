<?php
class Solution {
    function destCity($paths) {
        $starts = [];
        foreach ($paths as [$start, $end]) $starts[$start] = true;
        foreach ($paths as [$start, $end]) {
            if (!isset($starts[$end])) return $end;
        }
        return "";
    }
}
