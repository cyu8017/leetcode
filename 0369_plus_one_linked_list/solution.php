// LeetCode 0369 - Plus One Linked List
// https://leetcode.com/problems/plus-one-linked-list/

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
     * @param ListNode|null $head
     * @return ListNode|null
     */
    function plusOne($head) {
        return $this->plus_one($head);
    }

    /**
     * @param ListNode|null $head
     * @return ListNode|null
     */
    function plus_one($head) {
        $sentinel = new ListNode(0, $head);
        $notNine = $sentinel;
        $node = $head;

        while ($node !== null) {
            if ($node->val !== 9) {
                $notNine = $node;
            }
            $node = $node->next;
        }

        $notNine->val++;
        $node = $notNine->next;
        while ($node !== null) {
            $node->val = 0;
            $node = $node->next;
        }

        return $sentinel->val === 1 ? $sentinel : $sentinel->next;
    }
}
