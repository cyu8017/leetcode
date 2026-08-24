<?php
// LeetCode 2889 - Reshape Data: Pivot
// https://leetcode.com/problems/reshape-data-pivot/

class Solution {
    function pivotTable($weather) {
        $months = [];
        $byMonth = [];
        foreach ($weather as $r) {
            $city = (is_array($r) && isset($r[0]) && !isset($r['city'])) ? $r[0] : $r['city'];
            $month = (is_array($r) && isset($r[1]) && !isset($r['month'])) ? $r[1] : $r['month'];
            $temperature = (is_array($r) && isset($r[2]) && !isset($r['temperature'])) ? $r[2] : $r['temperature'];
            if (!isset($byMonth[$month])) {
                $byMonth[$month] = [];
                $months[] = $month;
            }
            $byMonth[$month][$city] = $temperature;
        }
        $out = [];
        foreach ($months as $month) {
            $row = ['month' => $month];
            foreach ($byMonth[$month] as $city => $temp) $row[$city] = $temp;
            $out[] = $row;
        }
        return $out;
    }
}
