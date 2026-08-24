<?php
// LeetCode 3072 - Distribute Elements Into Two Arrays II
// https://leetcode.com/problems/distribute-elements-into-two-arrays-ii/

class BIT {
    public $n;
    public $c;
    function __construct($n) {
        $this->n = $n;
        $this->c = array_fill(0, $n + 1, 0);
    }
    function update($x, $delta) {
        for (; $x <= $this->n; $x += $x & -$x) $this->c[$x] += $delta;
    }
    function query($x) {
        $s = 0;
        for (; $x > 0; $x -= $x & -$x) $s += $this->c[$x];
        return $s;
    }
}

class Solution {
    public $st;
    function resultArray($nums) {
        $this->st = $nums;
        sort($this->st);
        $n = count($this->st);
        $tree1 = new BIT($n + 1);
        $tree2 = new BIT($n + 1);
        $arr1 = [$nums[0]];
        $arr2 = [$nums[1]];
        $tree1->update($this->idx($nums[0]), 1);
        $tree2->update($this->idx($nums[1]), 1);
        $len = count($nums);
        for ($i = 2; $i < $len; $i++) {
            $x = $nums[$i];
            $id = $this->idx($x);
            $a = count($arr1) - $tree1->query($id);
            $b = count($arr2) - $tree2->query($id);
            if ($a > $b || ($a === $b && count($arr1) <= count($arr2))) {
                $arr1[] = $x;
                $tree1->update($id, 1);
            } else {
                $arr2[] = $x;
                $tree2->update($id, 1);
            }
        }
        return array_merge($arr1, $arr2);
    }
    function idx($x) {
        $lo = 0;
        $hi = count($this->st);
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi, 2);
            if ($this->st[$mid] < $x) $lo = $mid + 1;
            else $hi = $mid;
        }
        return $lo + 1;
    }
}
