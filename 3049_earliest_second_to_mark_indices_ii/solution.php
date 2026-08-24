<?php
// LeetCode 3049 - Earliest Second to Mark Indices II
// https://leetcode.com/problems/earliest-second-to-mark-indices-ii/

class MinHeap {
    public $a = [];
    function push($x) {
        $this->a[] = $x;
        $this->_up(count($this->a) - 1);
    }
    function pop() {
        if (count($this->a) === 0) return null;
        $top = $this->a[0];
        $last = array_pop($this->a);
        if (count($this->a) > 0) {
            $this->a[0] = $last;
            $this->_down(0);
        }
        return $top;
    }
    function size() {
        return count($this->a);
    }
    private function _up($i) {
        while ($i > 0) {
            $p = ($i - 1) >> 1;
            if ($this->a[$i] >= $this->a[$p]) break;
            $t = $this->a[$i];
            $this->a[$i] = $this->a[$p];
            $this->a[$p] = $t;
            $i = $p;
        }
    }
    private function _down($i) {
        $n = count($this->a);
        while (true) {
            $s = $i;
            $l = $i * 2 + 1;
            $r = $l + 1;
            if ($l < $n && $this->a[$l] < $this->a[$s]) $s = $l;
            if ($r < $n && $this->a[$r] < $this->a[$s]) $s = $r;
            if ($s === $i) break;
            $t = $this->a[$i];
            $this->a[$i] = $this->a[$s];
            $this->a[$s] = $t;
            $i = $s;
        }
    }
}

class Solution {
    private function getSecondToIndex($nums, $changeIndices) {
        $indexToFirstSecond = [];
        for ($second = 0; $second < count($changeIndices); $second++) {
            $index = $changeIndices[$second] - 1;
            if ($nums[$index] > 0 && !isset($indexToFirstSecond[$index])) {
                $indexToFirstSecond[$index] = $second;
            }
        }
        $secondToIndex = [];
        foreach ($indexToFirstSecond as $idx => $sec) $secondToIndex[$sec] = $idx;
        return $secondToIndex;
    }

    private function canMark($nums, $secondToIndex, $maxSecond, $numsSum) {
        $h = new MinHeap();
        $marks = 0;
        for ($second = $maxSecond - 1; $second >= 0; $second--) {
            if (isset($secondToIndex[$second])) {
                $h->push($nums[$secondToIndex[$second]]);
                if ($marks === 0) {
                    $h->pop();
                    $marks++;
                } else {
                    $marks--;
                }
            } else {
                $marks++;
            }
        }
        $heapSize = $h->size();
        $heapSum = 0;
        while ($h->size()) $heapSum += $h->pop();
        $decrementAndMarkCost = $numsSum - $heapSum + (count($nums) - $heapSize);
        $zeroAndMarkCost = $heapSize + $heapSize;
        return $decrementAndMarkCost + $zeroAndMarkCost <= $maxSecond;
    }

    function earliestSecondToMarkIndices($nums, $changeIndices) {
        $secondToIndex = $this->getSecondToIndex($nums, $changeIndices);
        $numsSum = 0;
        foreach ($nums as $v) $numsSum += $v;
        $l = 0;
        $r = count($changeIndices) + 1;
        while ($l < $r) {
            $m = intdiv($l + $r, 2);
            if ($this->canMark($nums, $secondToIndex, $m, $numsSum)) $r = $m;
            else $l = $m + 1;
        }
        return $l <= count($changeIndices) ? $l : -1;
    }
}
