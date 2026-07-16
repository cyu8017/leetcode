// LeetCode 0025 - Reverse Nodes in k-Group
// https://leetcode.com/problems/reverse-nodes-in-k-group/

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
     * @param ListNode $head
     * @param Integer $k
     * @return ListNode
     */
    function reverseKGroup($head, $k) {
        $dummy = new ListNode(0, $head);
        $groupPrevious = $dummy;

        while (true) {
            $kth = $groupPrevious;
            for ($i = 0; $i < $k; $i++) {
                $kth = $kth->next;
                if (!$kth) {
                    return $dummy->next;
                }
            }

            $groupNext = $kth->next;
            $previous = $groupNext;
            $current = $groupPrevious->next;

            while ($current !== $groupNext) {
                $next = $current->next;
                $current->next = $previous;
                $previous = $current;
                $current = $next;
            }

            $tmp = $groupPrevious->next;
            $groupPrevious->next = $kth;
            $groupPrevious = $tmp;
        }
    }
}
