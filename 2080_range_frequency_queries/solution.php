<?php
// LeetCode 2080 - Range Frequency Queries
// https://leetcode.com/problems/range-frequency-queries/

class RangeFreqQuery {
    private $pos = [];

    /**
     * @param Integer[] $arr
     */
    function __construct($arr) {
        $this->pos = [];
        $n = count($arr);
        for ($i = 0; $i < $n; $i++) $this->pos[$arr[$i]][] = $i;
    }

    private function lower($p, $x) {
        $lo = 0;
        $hi = count($p);
        while ($lo < $hi) {
            $mid = ($lo + $hi) >> 1;
            if ($p[$mid] < $x) $lo = $mid + 1;
            else $hi = $mid;
        }
        return $lo;
    }

    private function upper($p, $x) {
        $lo = 0;
        $hi = count($p);
        while ($lo < $hi) {
            $mid = ($lo + $hi) >> 1;
            if ($p[$mid] <= $x) $lo = $mid + 1;
            else $hi = $mid;
        }
        return $lo;
    }

    /**
     * @param Integer $left
     * @param Integer $right
     * @param Integer $value
     * @return Integer
     */
    function query($left, $right, $value) {
        if (!isset($this->pos[$value])) return 0;
        $p = $this->pos[$value];
        return $this->upper($p, $right) - $this->lower($p, $left);
    }
}
