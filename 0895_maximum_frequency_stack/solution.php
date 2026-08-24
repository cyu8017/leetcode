<?php
// LeetCode 0895 - Maximum Frequency Stack
// https://leetcode.com/problems/maximum-frequency-stack/

class FreqStack {
    private $freq = [];
    private $group = [];
    private $maxfreq = 0;

    function __construct() {
        $this->freq = [];
        $this->group = [];
        $this->maxfreq = 0;
    }

    function push($val) {
        $f = ($this->freq[$val] ?? 0) + 1;
        $this->freq[$val] = $f;
        $this->maxfreq = max($this->maxfreq, $f);
        if (!isset($this->group[$f])) $this->group[$f] = [];
        $this->group[$f][] = $val;
    }

    function pop() {
        $list = &$this->group[$this->maxfreq];
        $val = array_pop($list);
        $this->freq[$val]--;
        if (count($list) === 0) $this->maxfreq--;
        return $val;
    }
}
