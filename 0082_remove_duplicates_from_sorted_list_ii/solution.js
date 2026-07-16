// LeetCode 0082 - Remove Duplicates from Sorted List II
// https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

function ListNode(val, next) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
}

/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var deleteDuplicates = function(head) {
    const dummy = new ListNode(0, head);
    let previous = dummy;

    while (head) {
        if (head.next && head.val === head.next.val) {
            while (head.next && head.val === head.next.val) {
                head = head.next;
            }
            previous.next = head.next;
        } else {
            previous = previous.next;
        }
        head = head.next;
    }

    return dummy.next;
};
