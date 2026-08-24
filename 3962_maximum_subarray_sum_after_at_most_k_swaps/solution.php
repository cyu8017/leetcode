<?php
// LeetCode 3962 - Maximum Subarray Sum After at Most K Swaps
// https://leetcode.com/problems/maximum-subarray-sum-after-at-most-k-swaps/

class Solution {
    private $unique;

    function maxSubarraySum($nums, $k) {
        $n = count($nums);
        $unique = $nums;
        sort($unique);
        $u = [];
        foreach ($unique as $v) {
            if (empty($u) || $v != $u[count($u) - 1]) $u[] = $v;
        }
        $this->unique = $u;
        $rank = array_fill(0, $n, 0);
        $globalCount = array_fill(0, count($this->unique) + 1, 0);
        $globalSum = array_fill(0, count($this->unique) + 1, 0);
        for ($i = 0; $i < $n; $i++) {
            $rank[$i] = $this->lowerBound($this->unique, $nums[$i]) + 1;
            $this->add($globalCount, $globalSum, $rank[$i], 1);
        }
        $answer = -(1 << 60);
        for ($left = 0; $left < $n; $left++) {
            $insideCount = array_fill(0, count($this->unique) + 1, 0);
            $insideSum = array_fill(0, count($this->unique) + 1, 0);
            $outsideCount = $globalCount;
            $outsideSum = $globalSum;
            $subarraySum = 0;
            for ($right = $left; $right < $n; $right++) {
                $this->add($outsideCount, $outsideSum, $rank[$right], -1);
                $this->add($insideCount, $insideSum, $rank[$right], 1);
                $subarraySum += $nums[$right];
                $insideSize = $right - $left + 1;
                $outsideSize = $n - $insideSize;
                $limit = min($k, min($insideSize, $outsideSize));
                $low = 0;
                $high = $limit;
                while ($low < $high) {
                    $mid = intdiv($low + $high + 1, 2);
                    $insideValue = $this->unique[$this->kth($insideCount, $mid) - 1];
                    $outsideOrder = $outsideSize - $mid + 1;
                    $outsideValue = $this->unique[$this->kth($outsideCount, $outsideOrder) - 1];
                    if ($outsideValue > $insideValue) $low = $mid;
                    else $high = $mid - 1;
                }
                $swaps = $low;
                $gain = 0;
                if ($swaps > 0) {
                    $smallInside = $this->sumSmallest($insideCount, $insideSum, $swaps);
                    $totalOutside = $this->querySum($outsideSum, count($this->unique));
                    $largeOutside = $totalOutside - $this->sumSmallest($outsideCount, $outsideSum, $outsideSize - $swaps);
                    $gain = $largeOutside - $smallInside;
                }
                $answer = max($answer, $subarraySum + $gain);
            }
        }
        return $answer;
    }

    private function add(&$count, &$sum, $index, $delta) {
        $value = $this->unique[$index - 1];
        for (; $index < count($count); $index += $index & -$index) {
            $count[$index] += $delta;
            $sum[$index] += $delta * $value;
        }
    }

    private function queryCount($bit, $index) {
        $result = 0;
        for (; $index > 0; $index -= $index & -$index) $result += $bit[$index];
        return $result;
    }

    private function querySum($bit, $index) {
        $result = 0;
        for (; $index > 0; $index -= $index & -$index) $result += $bit[$index];
        return $result;
    }

    private function kth($bit, $order) {
        $index = 0;
        $step = 1;
        while (($step << 1) < count($bit)) $step <<= 1;
        for (; $step > 0; $step >>= 1) {
            $next = $index + $step;
            if ($next < count($bit) && $bit[$next] < $order) {
                $index = $next;
                $order -= $bit[$next];
            }
        }
        return $index + 1;
    }

    private function sumSmallest($count, $sum, $amount) {
        if ($amount <= 0) return 0;
        $index = $this->kth($count, $amount);
        $countBefore = $this->queryCount($count, $index - 1);
        $sumBefore = $this->querySum($sum, $index - 1);
        return $sumBefore + ($amount - $countBefore) * $this->unique[$index - 1];
    }

    private function lowerBound($a, $x) {
        $lo = 0;
        $hi = count($a);
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi, 2);
            if ($a[$mid] < $x) $lo = $mid + 1;
            else $hi = $mid;
        }
        return $lo;
    }
}
