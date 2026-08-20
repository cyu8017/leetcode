"use strict";
function deleteNodes(head, m, n) {
    let current = head;
    while (current) {
        for (let kept = 1; kept < m && current; kept++)
            current = current.next;
        if (!current)
            break;
        let removed = current.next;
        for (let count = 0; count < n && removed; count++)
            removed = removed.next;
        current.next = removed;
        current = removed;
    }
    return head;
}
