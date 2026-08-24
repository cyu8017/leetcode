<?php
// LeetCode 3414 - Maximum Score of Non-overlapping Intervals
// https://leetcode.com/problems/maximum-score-of-non-overlapping-intervals/

class Solution {
    private function copyState($s) {
        return ['score' => $s['score'], 'idx' => $s['idx']];
    }

    private function better($a, $b) {
        if ($a['score'] !== $b['score']) return $a['score'] > $b['score'] ? $a : $b;
        $m = min(count($a['idx']), count($b['idx']));
        for ($i = 0; $i < $m; $i++) {
            if ($a['idx'][$i] !== $b['idx'][$i]) return $a['idx'][$i] < $b['idx'][$i] ? $a : $b;
        }
        return count($a['idx']) <= count($b['idx']) ? $a : $b;
    }

    function maximumWeight($intervals) {
        $n = count($intervals);
        $arr = [];
        for ($i = 0; $i < $n; $i++) {
            $it = $intervals[$i];
            $arr[] = ['l' => $it[0], 'r' => $it[1], 'w' => $it[2], 'i' => $i];
        }
        usort($arr, function($a, $b) { return $a['r'] <=> $b['r']; });
        $empty = ['score' => 0, 'idx' => []];
        $dp = [];
        for ($i = 0; $i <= $n; $i++) {
            $dp[$i] = [];
            for ($t = 0; $t <= 4; $t++) $dp[$i][$t] = $this->copyState($empty);
        }
        for ($i = 1; $i <= $n; $i++) {
            $cur = $arr[$i - 1];
            for ($t = 0; $t <= 4; $t++) $dp[$i][$t] = $this->copyState($dp[$i - 1][$t]);
            $lo = 0;
            $hi = $i - 1;
            while ($lo < $hi) {
                $mid = intdiv($lo + $hi, 2);
                if ($arr[$mid]['r'] < $cur['l']) $lo = $mid + 1;
                else $hi = $mid;
            }
            $prev = $lo;
            for ($t = 1; $t <= 4; $t++) {
                $prevState = $dp[$prev][$t - 1];
                $cand = $this->copyState($prevState);
                $cand['score'] = $prevState['score'] + $cur['w'];
                $cand['idx'][] = $cur['i'];
                sort($cand['idx']);
                $dp[$i][$t] = $this->better($dp[$i][$t], $cand);
            }
        }
        $best = $dp[$n][0];
        for ($t = 1; $t <= 4; $t++) $best = $this->better($best, $dp[$n][$t]);
        return $best['idx'];
    }
}
