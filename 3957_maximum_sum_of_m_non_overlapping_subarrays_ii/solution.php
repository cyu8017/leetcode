<?php
// LeetCode 3957 - Maximum Sum of M Non-Overlapping Subarrays II
// https://leetcode.com/problems/maximum-sum-of-m-non-overlapping-subarrays-ii/

class Solution {
    function maxSum($nums, $m, $l, $r) {
        $n = count($nums);
        $prefix = array_fill(0, $n + 1, 0);
        for ($i = 0; $i < $n; $i++) $prefix[$i + 1] = $prefix[$i] + $nums[$i];
        $unconstrained = $this->run($prefix, $n, $l, $r, 0);
        if ($unconstrained[1] > 0 && $unconstrained[1] <= $m) return $unconstrained[0];
        if ($unconstrained[1] > $m) {
            $bound = 0;
            foreach ($nums as $value) $bound += $value >= 0 ? $value : -$value;
            $low = 0;
            $high = $bound + 1;
            while ($low < $high) {
                $mid = $low + intdiv($high - $low + 1, 2);
                if ($this->run($prefix, $n, $l, $r, $mid)[1] >= $m) $low = $mid;
                else $high = $mid - 1;
            }
            $state = $this->run($prefix, $n, $l, $r, $low);
            return $state[0] + $low * $m;
        }
        $infinity = 1 << 60;
        $bestSingle = -$infinity;
        $deque = [];
        for ($end = 1; $end <= $n; $end++) {
            $addIndex = $end - $l;
            if ($addIndex >= 0) {
                while (count($deque) > 0 && $prefix[$deque[count($deque) - 1]] >= $prefix[$addIndex]) array_pop($deque);
                $deque[] = $addIndex;
            }
            $minIndex = $end - $r;
            while (count($deque) > 0 && $deque[0] < $minIndex) array_shift($deque);
            if (count($deque) > 0) {
                $sum = $prefix[$end] - $prefix[$deque[0]];
                if ($sum > $bestSingle) $bestSingle = $sum;
            }
        }
        return $bestSingle;
    }

    private function better($a, $b) {
        return $a[0] > $b[0] || ($a[0] === $b[0] && $a[1] > $b[1]);
    }

    private function run($prefix, $n, $l, $r, $penalty) {
        $dp = array_fill(0, $n + 1, [0, 0]);
        $deque = [];
        for ($end = 1; $end <= $n; $end++) {
            $addIndex = $end - $l;
            if ($addIndex >= 0) {
                while (count($deque) > 0) {
                    $last = $deque[count($deque) - 1];
                    $left = [$dp[$addIndex][0] - $prefix[$addIndex], $dp[$addIndex][1]];
                    $right = [$dp[$last][0] - $prefix[$last], $dp[$last][1]];
                    if (!$this->better($left, $right)) break;
                    array_pop($deque);
                }
                $deque[] = $addIndex;
            }
            $minIndex = $end - $r;
            while (count($deque) > 0 && $deque[0] < $minIndex) array_shift($deque);
            $dp[$end] = [$dp[$end - 1][0], $dp[$end - 1][1]];
            if (count($deque) > 0) {
                $start = $deque[0];
                $take = [$dp[$start][0] + $prefix[$end] - $prefix[$start] - $penalty, $dp[$start][1] + 1];
                if ($this->better($take, $dp[$end])) $dp[$end] = $take;
            }
        }
        return $dp[$n];
    }
}
