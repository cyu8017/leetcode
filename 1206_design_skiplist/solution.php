<?php
// LeetCode 1206 - Design Skiplist
// https://leetcode.com/problems/design-skiplist/

class Skiplist {
    private $values = [];

    function __construct() {}

    /**
     * @param Integer $target
     * @return Boolean
     */
    function search($target) {
        $i = $this->bisectLeft($target);
        return $i < count($this->values) && $this->values[$i] === $target;
    }

    /**
     * @param Integer $num
     * @return NULL
     */
    function add($num) {
        $i = $this->bisectLeft($num);
        array_splice($this->values, $i, 0, [$num]);
    }

    /**
     * @param Integer $num
     * @return Boolean
     */
    function erase($num) {
        $i = $this->bisectLeft($num);
        if ($i === count($this->values) || $this->values[$i] !== $num) return false;
        array_splice($this->values, $i, 1);
        return true;
    }

    private function bisectLeft($target) {
        $lo = 0; $hi = count($this->values);
        while ($lo < $hi) {
            $mid = ($lo + $hi) >> 1;
            if ($this->values[$mid] < $target) $lo = $mid + 1;
            else $hi = $mid;
        }
        return $lo;
    }
}
