<?php
// LeetCode 1656 - Design an Ordered Stream
// https://leetcode.com/problems/design-an-ordered-stream/

class OrderedStream {
    private $a;
    private $p;

    function __construct($n) {
        $this->a = array_fill(0, $n + 1, null);
        $this->p = 1;
    }

    function insert($idKey, $value) {
        $this->a[$idKey] = $value;
        $out = [];
        while ($this->p < count($this->a) && $this->a[$this->p] !== null) {
            $out[] = $this->a[$this->p];
            $this->p++;
        }
        return $out;
    }
}
