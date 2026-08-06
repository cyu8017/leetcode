<?php

class TrieNode {
    /** @var TrieNode[] */
    public $child = [null, null];
    public $cnt = 0;
}

class Solution {
    /** @var TrieNode */
    private $trieRoot;
    private $BITS = 17;

    /**
     * @param Integer[] $parents
     * @param Integer[][] $queries
     * @return Integer[]
     */
    function maxGeneticDifference($parents, $queries) {
        $n = count($parents);
        $children = array_fill(0, $n, []);
        $root = 0;
        for ($i = 0; $i < $n; $i++) {
            $p = $parents[$i];
            if ($p === -1) {
                $root = $i;
            } else {
                $children[$p][] = $i;
            }
        }

        $qmap = array_fill(0, $n, []);
        foreach ($queries as $i => $q) {
            $qmap[$q[0]][] = [$i, $q[1]];
        }

        $ans = array_fill(0, count($queries), 0);
        $this->trieRoot = new TrieNode();

        $dfs = function ($u) use (&$dfs, &$children, &$qmap, &$ans) {
            $this->trieUpdate($u, 1);
            foreach ($qmap[$u] as $pair) {
                $ans[$pair[0]] = $this->trieMaxXor($pair[1]);
            }
            foreach ($children[$u] as $v) {
                $dfs($v);
            }
            $this->trieUpdate($u, -1);
        };

        $dfs($root);
        return $ans;
    }

    private function trieUpdate($num, $delta) {
        $node = $this->trieRoot;
        for ($b = $this->BITS; $b >= 0; $b--) {
            $bit = ($num >> $b) & 1;
            if ($node->child[$bit] === null) {
                $node->child[$bit] = new TrieNode();
            }
            $node = $node->child[$bit];
            $node->cnt += $delta;
        }
    }

    private function trieMaxXor($num) {
        $node = $this->trieRoot;
        $res = 0;
        for ($b = $this->BITS; $b >= 0; $b--) {
            $bit = ($num >> $b) & 1;
            $want = 1 - $bit;
            if ($node->child[$want] !== null && $node->child[$want]->cnt > 0) {
                $res |= 1 << $b;
                $node = $node->child[$want];
            } else {
                $node = $node->child[$bit];
            }
        }
        return $res;
    }
}
