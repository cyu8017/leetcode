// LeetCode 0086 - Partition List
// https://leetcode.com/problems/partition-list/

class ListNode {
    /** @var int */
    public $val = 0;
    /** @var ListNode|null */
    public $next = null;

    function __construct($val = 0, $next = null) {
        $this->val = $val;
        $this->next = $next;
    }
}

class Solution {
    /**
     * @param ListNode|null $head
     * @param Integer $x
     * @return ListNode|null
     */
    function partition($head, $x) {
        $beforeHead = new ListNode(0);
        $afterHead = new ListNode(0);
        $before = $beforeHead;
        $after = $afterHead;

        while ($head !== null) {
            if ($head->val < $x) {
                $before->next = $head;
                $before = $before->next;
            } else {
                $after->next = $head;
                $after = $after->next;
            }
            $head = $head->next;
        }

        $after->next = null;
        $before->next = $afterHead->next;
        return $beforeHead->next;
    }
}
