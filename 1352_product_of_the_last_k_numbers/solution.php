<?php
class ProductOfNumbers {
    private $p;

    function __construct() {
        $this->p = [1];
    }

    function add($num) {
        if ($num === 0) $this->p = [1];
        else $this->p[] = $this->p[count($this->p) - 1] * $num;
    }

    function getProduct($k) {
        $n = count($this->p);
        return $k >= $n ? 0 : intdiv($this->p[$n - 1], $this->p[$n - 1 - $k]);
    }
}
