<?php
// LeetCode 3762 - Minimum Operations to Equalize Subarrays
// https://leetcode.com/problems/minimum-operations-to-equalize-subarrays/

class _MONode {
    public $left = 0;
    public $right = 0;
    public $count = 0;
    public $sum = 0;
    function __construct($o = null) {
        if ($o) {
            $this->left = $o->left;
            $this->right = $o->right;
            $this->count = $o->count;
            $this->sum = $o->sum;
        }
    }
}

class Solution {
    function minOperations($nums, $k, $queries) {
        $n = count($nums);
        $quotient = array_fill(0, $n, 0);
        $remainder = array_fill(0, $n, 0);
        $values = array_fill(0, $n, 0);
        for ($i = 0; $i < $n; $i++) {
            $quotient[$i] = intdiv($nums[$i], $k);
            $remainder[$i] = $nums[$i] % $k;
            $values[$i] = $quotient[$i];
        }
        sort($values);
        $vu = 1;
        for ($i = 1; $i < $n; $i++) if ($values[$i] !== $values[$vu - 1]) $values[$vu++] = $values[$i];
        $values = array_slice($values, 0, $vu);

        $nodes = [new _MONode()];
        $roots = array_fill(0, $n + 1, 0);
        $umax = count($values) - 1;

        $lowerBound = function($a, $x) {
            $lo = 0;
            $hi = count($a);
            while ($lo < $hi) {
                $mid = ($lo + $hi) >> 1;
                if ($a[$mid] < $x) $lo = $mid + 1;
                else $hi = $mid;
            }
            return $lo;
        };

        $update = function($previous, $lo, $hi, $position, $value) use (&$update, &$nodes) {
            $current = count($nodes);
            $nodes[] = new _MONode($nodes[$previous]);
            $nodes[$current]->count++;
            $nodes[$current]->sum += $value;
            if ($lo < $hi) {
                $mid = ($lo + $hi) >> 1;
                if ($position <= $mid) $nodes[$current]->left = $update($nodes[$previous]->left, $lo, $mid, $position, $value);
                else $nodes[$current]->right = $update($nodes[$previous]->right, $mid + 1, $hi, $position, $value);
            }
            return $current;
        };

        $kth = function($rightRoot, $leftRoot, $lo, $hi, $rank) use (&$kth, &$nodes) {
            if ($lo === $hi) return $lo;
            $leftCount = $nodes[$nodes[$rightRoot]->left]->count - $nodes[$nodes[$leftRoot]->left]->count;
            $mid = ($lo + $hi) >> 1;
            if ($rank <= $leftCount) return $kth($nodes[$rightRoot]->left, $nodes[$leftRoot]->left, $lo, $mid, $rank);
            return $kth($nodes[$rightRoot]->right, $nodes[$leftRoot]->right, $mid + 1, $hi, $rank - $leftCount);
        };

        $prefixStats = function($rightRoot, $leftRoot, $lo, $hi, $end) use (&$prefixStats, &$nodes) {
            if ($end < $lo) return [0, 0];
            if ($hi <= $end) return [
                $nodes[$rightRoot]->count - $nodes[$leftRoot]->count,
                $nodes[$rightRoot]->sum - $nodes[$leftRoot]->sum
            ];
            $mid = ($lo + $hi) >> 1;
            $left = $prefixStats($nodes[$rightRoot]->left, $nodes[$leftRoot]->left, $lo, $mid, $end);
            $count = $left[0];
            $sum = $left[1];
            if ($end > $mid) {
                $right = $prefixStats($nodes[$rightRoot]->right, $nodes[$leftRoot]->right, $mid + 1, $hi, $end);
                $count += $right[0];
                $sum += $right[1];
            }
            return [$count, $sum];
        };

        for ($i = 0; $i < $n; $i++) {
            $position = $lowerBound($values, $quotient[$i]);
            $roots[$i + 1] = $update($roots[$i], 0, $umax, $position, $quotient[$i]);
        }

        $logv = array_fill(0, $n + 1, 0);
        for ($i = 2; $i <= $n; $i++) $logv[$i] = $logv[$i >> 1] + 1;
        $levels = $logv[$n] + 1;
        $minTable = [];
        $maxTable = [];
        $minTable[0] = $remainder;
        $maxTable[0] = $remainder;
        for ($level = 1; $level < $levels; $level++) {
            $length = $n - (1 << $level) + 1;
            $minTable[$level] = array_fill(0, $length, 0);
            $maxTable[$level] = array_fill(0, $length, 0);
            $half = 1 << ($level - 1);
            for ($i = 0; $i < $length; $i++) {
                $minTable[$level][$i] = min($minTable[$level - 1][$i], $minTable[$level - 1][$i + $half]);
                $maxTable[$level][$i] = max($maxTable[$level - 1][$i], $maxTable[$level - 1][$i + $half]);
            }
        }

        $answer = array_fill(0, count($queries), 0);
        for ($qi = 0; $qi < count($queries); $qi++) {
            $left = $queries[$qi][0];
            $right = $queries[$qi][1];
            $length = $right - $left + 1;
            $level = $logv[$length];
            $offset = $right - (1 << $level) + 1;
            $minR = min($minTable[$level][$left], $minTable[$level][$offset]);
            $maxR = max($maxTable[$level][$left], $maxTable[$level][$offset]);
            if ($minR !== $maxR) {
                $answer[$qi] = -1;
                continue;
            }
            $medianIndex = $kth($roots[$right + 1], $roots[$left], 0, $umax, intdiv($length + 1, 2));
            $median = $values[$medianIndex];
            $stats = $prefixStats($roots[$right + 1], $roots[$left], 0, $umax, $medianIndex);
            $leftCount = $stats[0];
            $leftSum = $stats[1];
            $totalSum = $nodes[$roots[$right + 1]]->sum - $nodes[$roots[$left]]->sum;
            $answer[$qi] = $median * $leftCount - $leftSum + ($totalSum - $leftSum) - $median * ($length - $leftCount);
        }
        return $answer;
    }
}
