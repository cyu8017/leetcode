// LeetCode 0369 - Plus One Linked List
function ListNode(val, next) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
}

var plusOne = function(head) {
    const sentinel = new ListNode(0, head);
    let notNine = sentinel;
    let node = head;

    while (node) {
        if (node.val !== 9) notNine = node;
        node = node.next;
    }

    notNine.val += 1;
    node = notNine.next;
    while (node) {
        node.val = 0;
        node = node.next;
    }

    return sentinel.val === 1 ? sentinel : sentinel.next;
};
