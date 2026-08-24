<?php
// LeetCode 3391 - Design a 3D Binary Matrix with Efficient Layer Tracking
// https://leetcode.com/problems/design-a-3d-binary-matrix-with-efficient-layer-tracking/

class Matrix3D {
    public $n;
    public $m;
    public $ones;

    function __construct($n) {
        $this->n = $n;
        $this->m = [];
        for ($x = 0; $x < $n; $x++) {
            $this->m[$x] = [];
            for ($y = 0; $y < $n; $y++) $this->m[$x][$y] = array_fill(0, $n, 0);
        }
        $this->ones = array_fill(0, $n, 0);
    }

    function setCell($x, $y, $z) {
        if ($this->m[$x][$y][$z] === 0) {
            $this->m[$x][$y][$z] = 1;
            $this->ones[$x]++;
        }
    }

    function unsetCell($x, $y, $z) {
        if ($this->m[$x][$y][$z] === 1) {
            $this->m[$x][$y][$z] = 0;
            $this->ones[$x]--;
        }
    }

    function largestMatrix() {
        $best = -1;
        $idx = 0;
        for ($i = 0; $i < $this->n; $i++) {
            if ($this->ones[$i] >= $best) {
                $best = $this->ones[$i];
                $idx = $i;
            }
        }
        return $idx;
    }
}
