<?php
class CustomStack {
    private $maxSize;
    private $a = [];

    function __construct($maxSize) {
        $this->maxSize = $maxSize;
        $this->a = [];
    }

    function push($x) {
        if (count($this->a) < $this->maxSize) $this->a[] = $x;
    }

    function pop() {
        return $this->a ? array_pop($this->a) : -1;
    }

    function increment($k, $val) {
        $limit = min($k, count($this->a));
        for ($i = 0; $i < $limit; $i++) $this->a[$i] += $val;
    }
}
