<?php
// LeetCode 1622 - Fancy Sequence
// https://leetcode.com/problems/fancy-sequence/

class Fancy {
    private $n = 0;
    private $size;
    private $tree;
    private $mul;
    private $add;
    private const MOD = 1000000007;

    function __construct() {
        $this->size = 1 << 17;
        $this->tree = array_fill(0, 2 * $this->size, 0);
        $this->mul = array_fill(0, 2 * $this->size, 1);
        $this->add = array_fill(0, 2 * $this->size, 0);
    }

    private function apply($p, $m, $a) {
        $this->tree[$p] = ($this->tree[$p] * $m + $a) % self::MOD;
        $this->mul[$p] = $this->mul[$p] * $m % self::MOD;
        $this->add[$p] = ($this->add[$p] * $m + $a) % self::MOD;
    }

    private function push($p) {
        if ($this->mul[$p] != 1 || $this->add[$p]) {
            $this->apply(2 * $p, $this->mul[$p], $this->add[$p]);
            $this->apply(2 * $p + 1, $this->mul[$p], $this->add[$p]);
            $this->mul[$p] = 1;
            $this->add[$p] = 0;
        }
    }

    private function update($p, $l, $r, $ql, $qr, $m, $a) {
        if ($ql <= $l && $r <= $qr) {
            $this->apply($p, $m, $a);
            return;
        }
        $this->push($p);
        $mid = intdiv($l + $r, 2);
        if ($ql <= $mid) {
            $this->update(2 * $p, $l, $mid, $ql, $qr, $m, $a);
        }
        if ($qr > $mid) {
            $this->update(2 * $p + 1, $mid + 1, $r, $ql, $qr, $m, $a);
        }
    }

    private function get($p, $l, $r, $i) {
        if ($l === $r) {
            return $this->tree[$p];
        }
        $this->push($p);
        $mid = intdiv($l + $r, 2);
        return $i <= $mid
            ? $this->get(2 * $p, $l, $mid, $i)
            : $this->get(2 * $p + 1, $mid + 1, $r, $i);
    }

    /**
     * @param Integer $val
     * @return NULL
     */
    function append($val) {
        $this->update(1, 0, $this->size - 1, $this->n, $this->n, 0, $val % self::MOD);
        $this->n++;
    }

    /**
     * @param Integer $inc
     * @return NULL
     */
    function addAll($inc) {
        if ($this->n) {
            $this->update(1, 0, $this->size - 1, 0, $this->n - 1, 1, $inc % self::MOD);
        }
    }

    /**
     * @param Integer $m
     * @return NULL
     */
    function multAll($m) {
        if ($this->n) {
            $this->update(1, 0, $this->size - 1, 0, $this->n - 1, $m % self::MOD, 0);
        }
    }

    /**
     * @param Integer $idx
     * @return Integer
     */
    function getIndex($idx) {
        return $idx < $this->n ? $this->get(1, 0, $this->size - 1, $idx) : -1;
    }
}
