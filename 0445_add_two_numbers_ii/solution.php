// LeetCode 0445 - Add Two Numbers II
// https://leetcode.com/problems/add-two-numbers-ii/

class ListNode {
    public $val = 0;
    public $next = null;
    function __construct($val = 0, $next = null) {
        $this->val = $val;
        $this->next = $next;
    }
}

class Solution {
    /**
     * @param ListNode $l1
     * @param ListNode $l2
     * @return ListNode
     */
    function addTwoNumbers($l1, $l2) {
        $stack1 = [];
        $stack2 = [];
        while ($l1) {
            $stack1[] = $l1->val;
            $l1 = $l1->next;
        }
        while ($l2) {
            $stack2[] = $l2->val;
            $l2 = $l2->next;
        }

        $carry = 0;
        $head = null;
        while (count($stack1) > 0 || count($stack2) > 0 || $carry) {
            $total = $carry;
            if (count($stack1) > 0) {
                $total += array_pop($stack1);
            }
            if (count($stack2) > 0) {
                $total += array_pop($stack2);
            }
            $carry = intdiv($total, 10);
            $node = new ListNode($total % 10, $head);
            $head = $node;
        }
        return $head;
    }
}
