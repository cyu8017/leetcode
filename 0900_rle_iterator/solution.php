<?php
// LeetCode 0900 - RLE Iterator
// https://leetcode.com/problems/rle-iterator/

class RLEIterator {
    private $enc;
    private $i;

    function __construct($encoding) {
        $this->enc = $encoding;
        $this->i = 0;
    }

    function next($n) {
        while ($this->i < count($this->enc)) {
            if ($this->enc[$this->i] >= $n) {
                $this->enc[$this->i] -= $n;
                return $this->enc[$this->i + 1];
            }
            $n -= $this->enc[$this->i];
            $this->i += 2;
        }
        return -1;
    }
}
