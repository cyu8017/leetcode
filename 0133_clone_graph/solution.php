<?php

class Node {
    public $val;
    public $neighbors;

    function __construct($val = 0, $neighbors = []) {
        $this->val = $val;
        $this->neighbors = $neighbors;
    }
}

class Solution {
    function cloneGraph($node) {
        if ($node === null) {
            return null;
        }
        $clones = [];

        $dfs = function ($current) use (&$dfs, &$clones) {
            $key = spl_object_id($current);
            if (isset($clones[$key])) {
                return $clones[$key];
            }

            $clone = new Node($current->val);
            $clones[$key] = $clone;
            foreach ($current->neighbors as $neighbor) {
                $clone->neighbors[] = $dfs($neighbor);
            }
            return $clone;
        };

        return $dfs($node);
    }
}