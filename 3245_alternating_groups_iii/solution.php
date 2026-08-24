<?php
// LeetCode 3245 - Alternating Groups III
// https://leetcode.com/problems/alternating-groups-iii/

class SegTree3245 {
    public $n;
    public $treeIntervalCounts;
    public $treeIntervalLengths;

    function __construct($n_) {
        $this->n = $n_;
        $this->treeIntervalCounts = array_fill(0, 4 * $n_, 0);
        $this->treeIntervalLengths = array_fill(0, 4 * $n_, 0);
    }

    function add($i, $val) { $this->addRec(0, 0, $this->n - 1, $i, $val); }

    function addRec($treeIndex, $lo, $hi, $i, $val) {
        if ($lo === $hi) {
            $this->treeIntervalCounts[$treeIndex] += $val;
            $this->treeIntervalLengths[$treeIndex] = $this->treeIntervalCounts[$treeIndex] * $i;
            return;
        }
        $mid = ($lo + $hi) >> 1;
        if ($i <= $mid) $this->addRec(2 * $treeIndex + 1, $lo, $mid, $i, $val);
        else $this->addRec(2 * $treeIndex + 2, $mid + 1, $hi, $i, $val);
        $this->treeIntervalCounts[$treeIndex] = $this->treeIntervalCounts[2 * $treeIndex + 1] + $this->treeIntervalCounts[2 * $treeIndex + 2];
        $this->treeIntervalLengths[$treeIndex] = $this->treeIntervalLengths[2 * $treeIndex + 1] + $this->treeIntervalLengths[2 * $treeIndex + 2];
    }

    function queryIntervalCounts($i) { return $this->query($this->treeIntervalCounts, 0, 0, $this->n - 1, $i, $this->n - 1); }
    function queryIntervalLengths($i) { return $this->query($this->treeIntervalLengths, 0, 0, $this->n - 1, $i, $this->n - 1); }

    function query($tree, $treeIndex, $lo, $hi, $i, $j) {
        if ($i <= $lo && $hi <= $j) return $tree[$treeIndex];
        if ($j < $lo || $hi < $i) return 0;
        $mid = ($lo + $hi) >> 1;
        return $this->query($tree, $treeIndex * 2 + 1, $lo, $mid, $i, $j) + $this->query($tree, $treeIndex * 2 + 2, $mid + 1, $hi, $i, $j);
    }
}

class Solution {
    private $n;
    private $arr;
    private $tree;
    private $intervals;

    function numberOfAlternatingGroups($colors, $queries) {
        $this->n = count($colors);
        $n = $this->n;
        $ans = [];
        $this->arr = array_fill(0, 2 * $n - 1, 0);
        for ($i = 0; $i < $n; $i++) $this->arr[$i] = $colors[$i];
        for ($i = 0; $i < $n - 1; $i++) $this->arr[$n + $i] = $colors[$i];
        $this->tree = new SegTree3245(2 * $n - 1);
        $this->intervals = [];
        $st = 0;
        for ($i = 1; $i < 2 * $n - 1; $i++) {
            if ($this->arr[$i] === $this->arr[$i - 1]) { $this->insert($st, $i - 1); $st = $i; }
        }
        $this->insert($st, 2 * $n - 2);
        foreach ($queries as $query) {
            if ($query[0] === 1) $ans[] = $this->getNum($query[1]);
            else {
                $index = $query[1];
                $color = $query[2];
                if ($this->arr[$index] !== $color) {
                    $this->update($index, $color);
                    if ($index < $n - 1) $this->update($index + $n, $color);
                }
            }
        }
        return $ans;
    }

    private function pack($l, $r) { return $l . ',' . $r; }

    private function unpack($k) {
        $p = explode(',', $k);
        return [(int)$p[0], (int)$p[1]];
    }

    private function insert($l, $r) {
        $this->intervals[$this->pack($l, $r)] = true;
        if ($l < $this->n) $this->tree->add($r - $l + 1, 1);
    }

    private function remove($l, $r) {
        unset($this->intervals[$this->pack($l, $r)]);
        if ($l < $this->n) $this->tree->add($r - $l + 1, -1);
    }

    private function findInterval($target) {
        $bestL = -1;
        $bestR = -1;
        foreach ($this->intervals as $k => $_) {
            [$kl, $kr] = $this->unpack($k);
            if ($kl <= $target && $target <= $kr && $kl > $bestL) { $bestL = $kl; $bestR = $kr; }
        }
        return [$bestL, $bestR];
    }

    private function getNum($sz) {
        $numIntervals = $this->tree->queryIntervalCounts($sz);
        $sumIntervals = $this->tree->queryIntervalLengths($sz);
        $numAlternatingGroups = $sumIntervals - $numIntervals * $sz + $numIntervals;
        [$l, $r] = $this->findInterval($this->n);
        if ($l < 0 || $l >= $this->n || $r - $l + 1 < $sz) return $numAlternatingGroups;
        if ($r >= $this->n) {
            $nonDuplicateGroups = $this->n - $l;
            $numGroups = ($r - $l + 1) - $sz + 1;
            $extra = $numGroups - $nonDuplicateGroups;
            if ($extra > 0) $numAlternatingGroups -= $extra;
        }
        return $numAlternatingGroups;
    }

    private function update($index, $color) {
        if ($this->arr[$index] === $color) return;
        $this->arr[$index] = $color;
        [$start, $end] = $this->findInterval($index);
        $this->remove($start, $end);
        if ($start < $index && $index < $end) {
            $this->insert($start, $index - 1);
            $this->insert($index, $index);
            $this->insert($index + 1, $end);
            return;
        }
        if ($start === $index && $index < $end) $this->insert($start + 1, $end);
        if ($start < $index && $index === $end) $this->insert($start, $end - 1);
        $ns = $index;
        $ne = $index;
        for (;;) {
            $merged = false;
            foreach (array_keys($this->intervals) as $k) {
                [$kl, $kr] = $this->unpack($k);
                if ($kr + 1 === $ns && $this->arr[$kr] !== $this->arr[$ns]) {
                    $this->remove($kl, $kr);
                    $ns = $kl;
                    $merged = true;
                    break;
                }
            }
            if (!$merged) break;
        }
        for (;;) {
            $merged = false;
            foreach (array_keys($this->intervals) as $k) {
                [$kl, $kr] = $this->unpack($k);
                if ($kl === $ne + 1 && $this->arr[$kl] !== $this->arr[$ne]) {
                    $this->remove($kl, $kr);
                    $ne = $kr;
                    $merged = true;
                    break;
                }
            }
            if (!$merged) break;
        }
        $this->insert($ns, $ne);
    }
}
