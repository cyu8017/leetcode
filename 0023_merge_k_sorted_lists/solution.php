// LeetCode 0023 - Merge k Sorted Lists
// https://leetcode.com/problems/merge-k-sorted-lists/

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
     * @param ListNode[] $lists
     * @return ListNode
     */
    function mergeKLists($lists) {
        $heap = new SplPriorityQueue();
        $heap->setExtractFlags(SplPriorityQueue::EXTR_DATA);
        $order = 0;

        foreach ($lists as $node) {
            if ($node) {
                $heap->insert($node, [-$node->val, -$order]);
                $order++;
            }
        }

        $dummy = new ListNode();
        $current = $dummy;

        while (!$heap->isEmpty()) {
            $node = $heap->extract();
            $current->next = $node;
            $current = $current->next;
            if ($node->next) {
                $heap->insert($node->next, [-$node->next->val, -$order]);
                $order++;
            }
        }

        return $dummy->next;
    }
}
