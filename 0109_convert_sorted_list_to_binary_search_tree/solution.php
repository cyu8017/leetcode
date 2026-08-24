<?php
// LeetCode 0109 - Convert Sorted List to Binary Search Tree
// https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/

class ListNode {
    public $val = 0;
    public $next = null;
    function __construct($val = 0, $next = null) {
        $this->val = $val;
        $this->next = $next;
    }
}

class TreeNode {
    public $val = 0;
    public $left = null;
    public $right = null;
    function __construct($val = 0, $left = null, $right = null) {
        $this->val = $val;
        $this->left = $left;
        $this->right = $right;
    }
}

class Solution {
    /**
     * @param ListNode $head
     * @return TreeNode
     */
    function sortedListToBST($head) {
        $values = [];
        while ($head !== null) {
            $values[] = $head->val;
            $head = $head->next;
        }
        return $this->build($values, 0, count($values) - 1);
    }

    private function build($values, $left, $right) {
        if ($left > $right) {
            return null;
        }
        $mid = intdiv($left + $right + 1, 2);
        $root = new TreeNode($values[$mid]);
        $root->left = $this->build($values, $left, $mid - 1);
        $root->right = $this->build($values, $mid + 1, $right);
        return $root;
    }
}
