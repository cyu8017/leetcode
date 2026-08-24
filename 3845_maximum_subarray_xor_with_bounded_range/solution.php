<?php
// LeetCode 3845 - Maximum Subarray XOR with Bounded Range
// https://leetcode.com/problems/maximum-subarray-xor-with-bounded-range/

class Solution {
    public $nodes;
    function add($x, $delta) {
        $u = 0;
        $this->nodes[$u]['count'] += $delta;
        for ($b = 15; $b >= 0; $b--) {
            $bit = ($x >> $b) & 1;
            if ($this->nodes[$u]['next'][$bit] === 0) {
                $this->nodes[$u]['next'][$bit] = count($this->nodes);
                $this->nodes[] = ['next' => [0, 0], 'count' => 0];
            }
            $u = $this->nodes[$u]['next'][$bit];
            $this->nodes[$u]['count'] += $delta;
        }
    }
    function query($x) {
        $u = 0;
        $res = 0;
        for ($b = 15; $b >= 0; $b--) {
            $bit = ($x >> $b) & 1;
            $want = $bit ^ 1;
            $v = $this->nodes[$u]['next'][$want];
            if ($v !== 0 && $this->nodes[$v]['count'] > 0) {
                $res |= 1 << $b;
                $u = $v;
            } else {
                $u = $this->nodes[$u]['next'][$bit];
            }
        }
        return $res;
    }
    function maxSubarrayXor($nums, $k) {
        $this->nodes = [['next' => [0, 0], 'count' => 0]];
        $n = count($nums);
        $pref = array_fill(0, $n + 1, 0);
        for ($i = 0; $i < $n; $i++) $pref[$i + 1] = $pref[$i] ^ $nums[$i];
        $maxQ = [];
        $minQ = [];
        $left = 0;
        $trieLeft = 0;
        $ans = 0;
        for ($r = 0; $r < $n; $r++) {
            $x = $nums[$r];
            while (count($maxQ) && $nums[$maxQ[count($maxQ) - 1]] <= $x) array_pop($maxQ);
            $maxQ[] = $r;
            while (count($minQ) && $nums[$minQ[count($minQ) - 1]] >= $x) array_pop($minQ);
            $minQ[] = $r;
            while ($nums[$maxQ[0]] - $nums[$minQ[0]] > $k) {
                if ($maxQ[0] === $left) array_shift($maxQ);
                if ($minQ[0] === $left) array_shift($minQ);
                $left++;
            }
            $this->add($pref[$r], 1);
            while ($trieLeft < $left) {
                $this->add($pref[$trieLeft], -1);
                $trieLeft++;
            }
            $cur = $this->query($pref[$r + 1]);
            if ($cur > $ans) $ans = $cur;
        }
        return $ans;
    }
}
