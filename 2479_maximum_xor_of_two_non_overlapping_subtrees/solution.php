<?php
// LeetCode 2479 - Maximum XOR of Two Non-Overlapping Subtrees
// https://leetcode.com/problems/maximum-xor-of-two-non-overlapping-subtrees/

class Solution {
    function maxXor($n, $edges, $values) {
        $g = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $g[$e[0]][] = $e[1];
            $g[$e[1]][] = $e[0];
        }
        $sum = array_fill(0, $n, 0);
        $dfsSum = function ($u, $p) use (&$dfsSum, &$g, $values, &$sum) {
            $s = $values[$u];
            foreach ($g[$u] as $v) if ($v !== $p) $s += $dfsSum($v, $u);
            $sum[$u] = $s;
            return $s;
        };
        $dfsSum(0, -1);
        $root = new stdClass();
        $root->child = [null, null];
        $insert = function ($x) use ($root) {
            $cur = $root;
            for ($b = 46; $b >= 0; $b--) {
                $bit = (int)(($x >> $b) & 1);
                if ($cur->child[$bit] === null) {
                    $node = new stdClass();
                    $node->child = [null, null];
                    $cur->child[$bit] = $node;
                }
                $cur = $cur->child[$bit];
            }
        };
        $query = function ($x) use ($root) {
            $cur = $root;
            if ($cur->child[0] === null && $cur->child[1] === null) return 0;
            $res = 0;
            for ($b = 46; $b >= 0; $b--) {
                $bit = (int)(($x >> $b) & 1);
                $want = $bit ^ 1;
                if ($cur->child[$want] !== null) {
                    $res |= 1 << $b;
                    $cur = $cur->child[$want];
                } elseif ($cur->child[$bit] !== null) {
                    $cur = $cur->child[$bit];
                } else {
                    return $res;
                }
            }
            return $res;
        };
        $ans = 0;
        $dfs = function ($u, $p) use (&$dfs, &$g, &$sum, $insert, $query, &$ans) {
            foreach ($g[$u] as $v) {
                if ($v === $p) continue;
                $xorv = $query($sum[$v]);
                if ($xorv > $ans) $ans = $xorv;
                $dfs($v, $u);
                $insert($sum[$v]);
            }
        };
        $dfs(0, -1);
        return $ans;
    }
}
