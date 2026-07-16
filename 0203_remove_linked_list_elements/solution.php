// LeetCode 0203 - Remove Linked List Elements
// https://leetcode.com/problems/remove-linked-list-elements/

class ListNode {
    public $val;
    public $next;

    function __construct($val = 0, $next = null) {
        $this->val = $val;
        $this->next = $next;
    }
}

class Solution {
    function removeElements($head, $val) {
        $dummy = new ListNode(0, $head);
        $current = $dummy;
        while ($current->next !== null) {
            if ($current->next->val === $val) {
                $current->next = $current->next->next;
            } else {
                $current = $current->next;
            }
        }
        return $dummy->next;
    }
}