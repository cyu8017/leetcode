// LeetCode 0023 - Merge k Sorted Lists
// https://leetcode.com/problems/merge-k-sorted-lists/

function ListNode(val, next) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
}

/**
 * @param {ListNode[]} lists
 * @return {ListNode}
 */
var mergeKLists = function(lists) {
    const heap = [];
    let counter = 0;

    function heapPush(entry) {
        heap.push(entry);
        let i = heap.length - 1;
        while (i > 0) {
            const parent = Math.floor((i - 1) / 2);
            if (
                heap[parent][0] < heap[i][0] ||
                (heap[parent][0] === heap[i][0] && heap[parent][1] < heap[i][1])
            ) {
                break;
            }
            [heap[parent], heap[i]] = [heap[i], heap[parent]];
            i = parent;
        }
    }

    function heapPop() {
        const top = heap[0];
        const last = heap.pop();
        if (heap.length > 0) {
            heap[0] = last;
            let i = 0;
            while (true) {
                let smallest = i;
                const left = 2 * i + 1;
                const right = 2 * i + 2;
                if (
                    left < heap.length &&
                    (heap[left][0] < heap[smallest][0] ||
                        (heap[left][0] === heap[smallest][0] &&
                            heap[left][1] < heap[smallest][1]))
                ) {
                    smallest = left;
                }
                if (
                    right < heap.length &&
                    (heap[right][0] < heap[smallest][0] ||
                        (heap[right][0] === heap[smallest][0] &&
                            heap[right][1] < heap[smallest][1]))
                ) {
                    smallest = right;
                }
                if (smallest === i) {
                    break;
                }
                [heap[i], heap[smallest]] = [heap[smallest], heap[i]];
                i = smallest;
            }
        }
        return top;
    }

    for (const node of lists) {
        if (node) {
            heapPush([node.val, counter, node]);
            counter++;
        }
    }

    const dummy = new ListNode();
    let current = dummy;

    while (heap.length > 0) {
        const node = heapPop()[2];
        current.next = node;
        current = current.next;
        if (node.next) {
            heapPush([node.next.val, counter, node.next]);
            counter++;
        }
    }

    return dummy.next;
};
