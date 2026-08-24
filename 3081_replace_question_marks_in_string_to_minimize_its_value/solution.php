<?php
// LeetCode 3081 - Replace Question Marks in String to Minimize Its Value
// https://leetcode.com/problems/replace-question-marks-in-string-to-minimize-its-value/

class MinHeap {
    public $a = [];
    public $cmp;
    function __construct($cmp = null) {
        $this->cmp = $cmp;
    }
    function _up($i) {
        $a = &$this->a;
        $cmp = $this->cmp;
        while ($i > 0) {
            $p = ($i - 1) >> 1;
            $c = $cmp ? $cmp($a[$i], $a[$p]) : ($a[$i] <=> $a[$p]);
            if ($c >= 0) break;
            $t = $a[$i]; $a[$i] = $a[$p]; $a[$p] = $t;
            $i = $p;
        }
    }
    function _down($i) {
        $a = &$this->a;
        $cmp = $this->cmp;
        $n = count($a);
        while (true) {
            $s = $i; $l = $i * 2 + 1; $r = $l + 1;
            if ($l < $n) {
                $c = $cmp ? $cmp($a[$l], $a[$s]) : ($a[$l] <=> $a[$s]);
                if ($c < 0) $s = $l;
            }
            if ($r < $n) {
                $c = $cmp ? $cmp($a[$r], $a[$s]) : ($a[$r] <=> $a[$s]);
                if ($c < 0) $s = $r;
            }
            if ($s === $i) break;
            $t = $a[$i]; $a[$i] = $a[$s]; $a[$s] = $t;
            $i = $s;
        }
    }
    function push($x) { $this->a[] = $x; $this->_up(count($this->a) - 1); }
    function pop() {
        $a = &$this->a;
        if (!$a) return null;
        $top = $a[0];
        $last = array_pop($a);
        if ($a) { $a[0] = $last; $this->_down(0); }
        return $top;
    }
    function peek() { return $this->a[0]; }
    function size() { return count($this->a); }
}

class Solution {
    function minimizeStringValue($s) {
        $cnt = array_fill(0, 26, 0);
        $k = 0;
        $len = strlen($s);
        for ($i = 0; $i < $len; $i++) {
            $c = $s[$i];
            if ($c === "?") $k++;
            else $cnt[ord($c) - 97]++;
        }
        $pq = new MinHeap(function ($a, $b) {
            return $a[0] !== $b[0] ? $a[0] <=> $b[0] : $a[1] <=> $b[1];
        });
        for ($i = 0; $i < 26; $i++) $pq->push([$cnt[$i], $i]);
        $t = array_fill(0, $k, 0);
        for ($i = 0; $i < $k; $i++) {
            $p = $pq->pop();
            $t[$i] = $p[1];
            $p[0]++;
            $pq->push($p);
        }
        sort($t);
        $arr = str_split($s);
        $j = 0;
        for ($i = 0; $i < count($arr); $i++) {
            if ($arr[$i] === "?") {
                $arr[$i] = chr($t[$j] + 97);
                $j++;
            }
        }
        return implode("", $arr);
    }
}
