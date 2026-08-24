<?php
// LeetCode 3943 - Number of Pairs After Increment
// https://leetcode.com/problems/number-of-pairs-after-increment/

class Solution {
    function numberOfPairs($nums1, $nums2, $queries) {
        $blockSize = 225;
        $n = count($nums2);
        $blocks = intdiv($n + $blockSize - 1, $blockSize);
        $lazy = array_fill(0, $blocks, 0);
        $freq = array_fill(0, $blocks, []);
        for ($b = 0; $b < $blocks; $b++) $this->rebuild($freq, $nums2, $b, $blockSize, $n);
        $fixed = [];
        foreach ($nums1 as $x) $fixed[$x] = ($fixed[$x] ?? 0) + 1;
        $answer = [];
        foreach ($queries as $q) {
            if ($q[0] === 1) {
                $l = $q[1];
                $r = $q[2];
                $delta = $q[3];
                $first = intdiv($l, $blockSize);
                $last = intdiv($r, $blockSize);
                if ($first === $last) {
                    $this->push($lazy, $nums2, $first, $blockSize, $n);
                    for ($i = $l; $i <= $r; $i++) $nums2[$i] += $delta;
                    $this->rebuild($freq, $nums2, $first, $blockSize, $n);
                    continue;
                }
                $this->push($lazy, $nums2, $first, $blockSize, $n);
                for ($i = $l; $i < ($first + 1) * $blockSize; $i++) $nums2[$i] += $delta;
                $this->rebuild($freq, $nums2, $first, $blockSize, $n);
                $this->push($lazy, $nums2, $last, $blockSize, $n);
                for ($i = $last * $blockSize; $i <= $r; $i++) $nums2[$i] += $delta;
                $this->rebuild($freq, $nums2, $last, $blockSize, $n);
                for ($b = $first + 1; $b < $last; $b++) $lazy[$b] += $delta;
            } else {
                $total = 0;
                foreach ($fixed as $a => $countA) {
                    $target = $q[1] - $a;
                    for ($b = 0; $b < $blocks; $b++) {
                        $key = $target - $lazy[$b];
                        if (isset($freq[$b][$key])) $total += $countA * $freq[$b][$key];
                    }
                }
                $answer[] = $total;
            }
        }
        return $answer;
    }

    private function rebuild(&$freq, $nums2, $b, $blockSize, $n) {
        $freq[$b] = [];
        $end = min(($b + 1) * $blockSize, $n);
        for ($i = $b * $blockSize; $i < $end; $i++) {
            $freq[$b][$nums2[$i]] = ($freq[$b][$nums2[$i]] ?? 0) + 1;
        }
    }

    private function push(&$lazy, &$nums2, $b, $blockSize, $n) {
        if ($lazy[$b] !== 0) {
            $end = min(($b + 1) * $blockSize, $n);
            for ($i = $b * $blockSize; $i < $end; $i++) $nums2[$i] += $lazy[$b];
            $lazy[$b] = 0;
        }
    }
}
