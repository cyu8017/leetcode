<?php
// LeetCode 3929 - Minimum Partition Score II
// https://leetcode.com/problems/minimum-partition-score-ii/

class Solution {
    function minPartitionScore($nums, $k) {
        $n = count($nums);
        $prefix = array_fill(0, $n + 1, 0);
        for ($i = 0; $i < $n; $i++) $prefix[$i + 1] = $prefix[$i] + $nums[$i];

        $bound = $prefix[$n] * $prefix[$n] + $prefix[$n] + 1;
        $low = 0;
        $high = $bound;
        while ($low < $high) {
            $mid = $low + intdiv($high - $low + 1, 2);
            if ($this->run($prefix, $n, $mid)[1] >= $k) $low = $mid;
            else $high = $mid - 1;
        }
        $state = $this->run($prefix, $n, $low);
        return intdiv($state[0] - $low * $k, 2);
    }

    private function better($a, $b) {
        if (!$a[2]) return $b;
        if (!$b[2]) return $a;
        if ($a[0] !== $b[0]) return $a[0] < $b[0] ? $a : $b;
        return $a[1] >= $b[1] ? $a : $b;
    }

    private function evaluate($line, $x) {
        if (!$line[3]) return [0, 0, false];
        return [$line[0] * $x + $line[1], $line[2], true];
    }

    private function insert(&$tree, $node, $left, $right, $line, $prefix) {
        if (!$tree[$node][3]) {
            $tree[$node] = $line;
            return;
        }
        $mid = intdiv($left + $right, 2);
        $xLeft = $prefix[$left];
        $xMid = $prefix[$mid];
        $leftBetter = $this->better($this->evaluate($line, $xLeft), $this->evaluate($tree[$node], $xLeft));
        $midBetter = $this->better($this->evaluate($line, $xMid), $this->evaluate($tree[$node], $xMid));
        $el = $this->evaluate($line, $xLeft);
        $em = $this->evaluate($line, $xMid);
        $lineWinsLeft = $leftBetter[0] === $el[0] && $leftBetter[1] === $line[2];
        $lineWinsMid = $midBetter[0] === $em[0] && $midBetter[1] === $line[2];
        if ($lineWinsMid) {
            $tmp = $tree[$node];
            $tree[$node] = $line;
            $line = $tmp;
        }
        if ($left === $right) return;
        if ($lineWinsLeft !== $lineWinsMid) $this->insert($tree, $node * 2, $left, $mid, $line, $prefix);
        else $this->insert($tree, $node * 2 + 1, $mid + 1, $right, $line, $prefix);
    }

    private function query($tree, $node, $left, $right, $index, $prefix) {
        $result = $this->evaluate($tree[$node], $prefix[$index]);
        if ($left === $right) return $result;
        $mid = intdiv($left + $right, 2);
        if ($index <= $mid) return $this->better($result, $this->query($tree, $node * 2, $left, $mid, $index, $prefix));
        return $this->better($result, $this->query($tree, $node * 2 + 1, $mid + 1, $right, $index, $prefix));
    }

    private function run($prefix, $n, $penalty) {
        $tree = array_fill(0, 4 * ($n + 1), [0, 0, 0, false]);
        $this->insert($tree, 1, 0, $n, [0, 0, 0, true], $prefix);
        $current = [0, 0, false];
        for ($i = 1; $i <= $n; $i++) {
            $best = $this->query($tree, 1, 0, $n, $i, $prefix);
            $x = $prefix[$i];
            $current = [$best[0] + $x * $x + $x + $penalty, $best[1] + 1, true];
            $this->insert($tree, 1, 0, $n, [-2 * $x, $current[0] + $x * $x - $x, $current[1], true], $prefix);
        }
        return $current;
    }
}
