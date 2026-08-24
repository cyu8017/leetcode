<?php
// LeetCode 2213 - Longest Substring of One Repeating Character
// https://leetcode.com/problems/longest-substring-of-one-repeating-character/

class Solution {
    function longestRepeating($s_, $queryCharacters, $queryIndices) {
        $merge = function($a, $b) {
            if ($a === null || ($a['size'] ?? 0) === 0) return $b;
            if ($b === null || ($b['size'] ?? 0) === 0) return $a;
            $res = [
                'lChar' => $a['lChar'],
                'rChar' => $b['rChar'],
                'size' => $a['size'] + $b['size'],
                'best' => max($a['best'], $b['best']),
                'lLen' => $a['lLen'],
                'rLen' => $b['rLen'],
            ];
            if ($a['rChar'] === $b['lChar']) {
                $mid = $a['rLen'] + $b['lLen'];
                $res['best'] = max($res['best'], $mid);
                if ($a['lLen'] === $a['size']) $res['lLen'] = $a['size'] + $b['lLen'];
                if ($b['rLen'] === $b['size']) $res['rLen'] = $b['size'] + $a['rLen'];
            }
            return $res;
        };
        $s = str_split($s_);
        $n = count($s);
        $tree = array_fill(0, 4 * $n + 5, null);
        $build = function($idx, $l, $r) use (&$build, &$tree, &$s, $merge) {
            if ($l === $r) {
                $tree[$idx] = ['lChar' => $s[$l], 'rChar' => $s[$l], 'lLen' => 1, 'rLen' => 1, 'best' => 1, 'size' => 1];
                return;
            }
            $mid = ($l + $r) >> 1;
            $build($idx * 2, $l, $mid);
            $build($idx * 2 + 1, $mid + 1, $r);
            $tree[$idx] = $merge($tree[$idx * 2], $tree[$idx * 2 + 1]);
        };
        $update = function($idx, $l, $r, $pos, $ch) use (&$update, &$tree, &$s, $merge) {
            if ($l === $r) {
                $s[$pos] = $ch;
                $tree[$idx] = ['lChar' => $ch, 'rChar' => $ch, 'lLen' => 1, 'rLen' => 1, 'best' => 1, 'size' => 1];
                return;
            }
            $mid = ($l + $r) >> 1;
            if ($pos <= $mid) $update($idx * 2, $l, $mid, $pos, $ch);
            else $update($idx * 2 + 1, $mid + 1, $r, $pos, $ch);
            $tree[$idx] = $merge($tree[$idx * 2], $tree[$idx * 2 + 1]);
        };
        $build(1, 0, $n - 1);
        $ans = array_fill(0, count($queryIndices), 0);
        for ($i = 0; $i < count($queryIndices); $i++) {
            $update(1, 0, $n - 1, $queryIndices[$i], $queryCharacters[$i]);
            $ans[$i] = $tree[1]['best'];
        }
        return $ans;
    }
}
