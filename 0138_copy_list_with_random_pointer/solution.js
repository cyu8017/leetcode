// LeetCode 0138 - Copy List with Random Pointer
// https://leetcode.com/problems/copy-list-with-random-pointer/

function Node(val = 0, next = null, random = null) {
    this.val = val;
    this.next = next;
    this.random = random;
}

/**
 * @param {Node|null} head
 * @return {Node|null}
 */
var copyRandomList = function(head) {
    const clones = new Map();

    const clone = (node) => {
        if (!node) return null;
        if (clones.has(node)) return clones.get(node);

        const copy = new Node(node.val);
        clones.set(node, copy);
        copy.next = clone(node.next);
        copy.random = clone(node.random);
        return copy;
    };

    return clone(head);
};