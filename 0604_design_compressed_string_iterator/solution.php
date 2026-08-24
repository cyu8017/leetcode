<?php
// LeetCode 0604 - Design Compressed String Iterator
// https://leetcode.com/problems/design-compressed-string-iterator/

class StringIterator {
    private $chars = [];
    private $counts = [];
    private $index = 0;

    function __construct($compressedString) {
        $i = 0;
        $n = strlen($compressedString);
        while ($i < $n) {
            $ch = $compressedString[$i++];
            $j = $i;
            while ($j < $n && $compressedString[$j] >= "0" && $compressedString[$j] <= "9") ++$j;
            $this->chars[] = $ch;
            $this->counts[] = intval(substr($compressedString, $i, $j - $i));
            $i = $j;
        }
    }

    function next() {
        if (!$this->hasNext()) return " ";
        $ch = $this->chars[$this->index];
        $this->counts[$this->index] -= 1;
        if ($this->counts[$this->index] === 0) ++$this->index;
        return $ch;
    }

    function hasNext() {
        return $this->index < count($this->chars);
    }
}
