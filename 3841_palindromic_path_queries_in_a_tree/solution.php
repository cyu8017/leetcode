<?php
// LeetCode 3841 - Palindromic Path Queries in a Tree
// https://leetcode.com/problems/palindromic-path-queries-in-a-tree/

class Solution {
    public $bit;
    public $n;
    public $parent;
    public $depth;
    public $head;
    public $position;
    function update($index, $value) {
        for ($index++; $index <= $this->n; $index += $index & -$index) $this->bit[$index] ^= $value;
    }
    function prefix($index) {
        $result = 0;
        for (; $index > 0; $index -= $index & -$index) $result ^= $this->bit[$index];
        return $result;
    }
    function pathMask($u, $v) {
        $result = 0;
        while ($this->head[$u] !== $this->head[$v]) {
            if ($this->depth[$this->head[$u]] < $this->depth[$this->head[$v]]) { $tmp = $u; $u = $v; $v = $tmp; }
            $result ^= $this->prefix($this->position[$u] + 1) ^ $this->prefix($this->position[$this->head[$u]]);
            $u = $this->parent[$this->head[$u]];
        }
        if ($this->position[$u] > $this->position[$v]) { $tmp = $u; $u = $v; $v = $tmp; }
        return $result ^ $this->prefix($this->position[$v] + 1) ^ $this->prefix($this->position[$u]);
    }
    function palindromicPathQueries($n, $edges, $s, $queries) {
        $this->n = $n;
        $graph = [];
        for ($i = 0; $i < $n; $i++) $graph[$i] = [];
        foreach ($edges as $edge) {
            $graph[$edge[0]][] = $edge[1];
            $graph[$edge[1]][] = $edge[0];
        }
        $parent = array_fill(0, $n, -2);
        $depth = array_fill(0, $n, 0);
        $parent[0] = -1;
        $order = [0];
        for ($i = 0; $i < count($order); $i++) {
            $u = $order[$i];
            foreach ($graph[$u] as $v) {
                if ($parent[$v] === -2) {
                    $parent[$v] = $u;
                    $depth[$v] = $depth[$u] + 1;
                    $order[] = $v;
                }
            }
        }
        $size = array_fill(0, $n, 0);
        $heavy = array_fill(0, $n, -1);
        for ($i = $n - 1; $i >= 0; $i--) {
            $u = $order[$i];
            $size[$u] = 1;
            foreach ($graph[$u] as $v) {
                if ($parent[$v] === $u) {
                    $size[$u] += $size[$v];
                    if ($heavy[$u] === -1 || $size[$v] > $size[$heavy[$u]]) $heavy[$u] = $v;
                }
            }
        }
        $head = array_fill(0, $n, 0);
        $position = array_fill(0, $n, 0);
        $stack = [[0, 0]];
        $nextPosition = 0;
        while (count($stack)) {
            $chain = array_pop($stack);
            for ($u = $chain[0]; $u !== -1; $u = $heavy[$u]) {
                $head[$u] = $chain[1];
                $position[$u] = $nextPosition++;
                foreach ($graph[$u] as $v) {
                    if ($parent[$v] === $u && $v !== $heavy[$u]) $stack[] = [$v, $v];
                }
            }
        }
        $this->parent = $parent;
        $this->depth = $depth;
        $this->head = $head;
        $this->position = $position;
        $this->bit = array_fill(0, $n + 1, 0);
        $current = [];
        for ($i = 0; $i < $n; $i++) $current[] = $s[$i];
        for ($node = 0; $node < $n; $node++) $this->update($position[$node], 1 << (ord($current[$node]) - 97));
        $answer = [];
        foreach ($queries as $query) {
            $parts = explode(' ', $query);
            $op = $parts[0];
            $node = intval($parts[1]);
            if ($op === 'update') {
                $newCharacter = $parts[2][0];
                $delta = (1 << (ord($current[$node]) - 97)) ^ (1 << (ord($newCharacter) - 97));
                $this->update($position[$node], $delta);
                $current[$node] = $newCharacter;
            } else {
                $other = intval($parts[2]);
                $mask = $this->pathMask($node, $other);
                $answer[] = (($mask & ($mask - 1)) === 0);
            }
        }
        return $answer;
    }
}
