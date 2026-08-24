<?php
// LeetCode 2424 - Longest Uploaded Prefix
// https://leetcode.com/problems/longest-uploaded-prefix/

class LUPrefix {
    private $uploaded;
    private $prefixLen;

    function __construct($n) {
        $this->uploaded = array_fill(0, $n + 2, false);
        $this->prefixLen = 0;
    }

    function upload($video) {
        $this->uploaded[$video] = true;
        while ($this->uploaded[$this->prefixLen + 1]) $this->prefixLen++;
    }

    function longest() {
        return $this->prefixLen;
    }
}
