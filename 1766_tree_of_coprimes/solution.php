<?php
// LeetCode 1766 - Tree of Coprimes
// https://leetcode.com/problems/tree-of-coprimes/

class Solution {
    private $adj;
    private $nums;
    private $ans;
    private $path;

    /**
     * @param Integer[] $nums
     * @param Integer[][] $edges
     * @return Integer[]
     */
    function getCoprimes($nums, $edges) {
        $n = count($nums);
        $this->nums = $nums;
        $this->adj = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $this->adj[$e[0]][] = $e[1];
            $this->adj[$e[1]][] = $e[0];
        }
        $this->ans = array_fill(0, $n, -1);
        $this->path = array_fill(0, 51, []);
        $this->dfs(0, -1, 0);
        return $this->ans;
    }

    private function dfs($node, $parent, $depth) {
        $bestDepth = -1;
        $bestNode = -1;
        $val = $this->nums[$node];
        for ($d = 1; $d <= 50; $d++) {
            if ($this->gcd($val, $d) === 1 && count($this->path[$d]) > 0) {
                [$candDepth, $candNode] = end($this->path[$d]);
                if ($candDepth > $bestDepth) {
                    $bestDepth = $candDepth;
                    $bestNode = $candNode;
                }
            }
        }
        $this->ans[$node] = $bestNode;
        $this->path[$val][] = [$depth, $node];
        foreach ($this->adj[$node] as $nxt) {
            if ($nxt !== $parent) {
                $this->dfs($nxt, $node, $depth + 1);
            }
        }
        array_pop($this->path[$val]);
    }

    private function gcd($a, $b) {
        while ($b !== 0) {
            $t = $a % $b;
            $a = $b;
            $b = $t;
        }
        return $a;
    }
}
