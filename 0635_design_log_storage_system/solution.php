<?php
// LeetCode 0635 - Design Log Storage System
// https://leetcode.com/problems/design-log-storage-system/

class LogSystem {
    private $ids = [];
    private $timestamps = [];
    private $granularityIndex = [
        "Year" => 4, "Month" => 7, "Day" => 10, "Hour" => 13, "Minute" => 16, "Second" => 19
    ];

    function __construct() {}

    function put($id, $timestamp) {
        $this->ids[] = $id;
        $this->timestamps[] = $timestamp;
    }

    function retrieve($start, $end, $granularity) {
        $index = $this->granularityIndex[$granularity];
        $startKey = substr($start, 0, $index);
        $endKey = substr($end, 0, $index);
        $matched = [];
        for ($i = 0; $i < count($this->timestamps); ++$i) {
            $timestamp = $this->timestamps[$i];
            $key = substr($timestamp, 0, $index);
            if ($startKey <= $key && $key <= $endKey) $matched[] = [$timestamp, $this->ids[$i]];
        }
        usort($matched, function($a, $b) { return $a[0] <=> $b[0]; });
        $result = [];
        foreach ($matched as $item) $result[] = $item[1];
        return $result;
    }
}
