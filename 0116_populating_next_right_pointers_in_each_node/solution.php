<?php
class Node {
    public $val = 0;
    public $left = null;
    public $right = null;
    public $next = null;
    function __construct($val = 0, $left = null, $right = null, $next = null) {
        $this->val = $val; $this->left = $left; $this->right = $right; $this->next = $next;
    }
}

class Solution {
    function connect($root) {
        if ($root === null) return null;
        $level = [$root];
        while (!empty($level)) {
            $count = count($level);
            for ($i = 0; $i < $count; $i++) {
                $level[$i]->next = $i + 1 < $count ? $level[$i + 1] : null;
            }
            $nextLevel = [];
            foreach ($level as $node) {
                if ($node->left !== null) $nextLevel[] = $node->left;
                if ($node->right !== null) $nextLevel[] = $node->right;
            }
            $level = $nextLevel;
        }
        return $root;
    }
}
