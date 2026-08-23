// LeetCode 2074 - Reverse Nodes in Even Length Groups
// https://leetcode.com/problems/reverse-nodes-in-even-length-groups/

/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseEvenLengthGroups = function(head) {
    const dummy = new ListNode(0, head);
    let prev = dummy;
    let group = 1;
    while (prev.next) {
        const cur = prev.next;
        let cnt = 0;
        let node = cur;
        while (node && cnt < group) { node = node.next; cnt++; }
        if (cnt % 2 === 0) {
            let revPrev = node;
            let p = cur;
            for (let i = 0; i < cnt; i++) {
                const nxt = p.next;
                p.next = revPrev;
                revPrev = p;
                p = nxt;
            }
            prev.next = revPrev;
            prev = cur;
        } else {
            for (let i = 0; i < cnt; i++) prev = prev.next;
        }
        group++;
    }
    return dummy.next;
};
