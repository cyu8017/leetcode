// LeetCode 0023 - Merge k Sorted Lists
// https://leetcode.com/problems/merge-k-sorted-lists/

class ListNode {
    var val: Int
    var next: ListNode?
    init() { val = 0; next = nil }
    init(_ val: Int) { self.val = val; next = nil }
    init(_ val: Int, _ next: ListNode?) { self.val = val; self.next = next }
}

class Solution {
    func mergeKLists(_ lists: [ListNode?]) -> ListNode? {
        var heap: [(Int, Int, ListNode)] = []
        var order = 0

        func push(_ node: ListNode) {
            heap.append((node.val, order, node))
            order += 1
            var index = heap.count - 1
            while index > 0 {
                let parent = (index - 1) / 2
                if heap[index].0 < heap[parent].0 ||
                    (heap[index].0 == heap[parent].0 && heap[index].1 < heap[parent].1) {
                    heap.swapAt(index, parent)
                    index = parent
                } else {
                    break
                }
            }
        }

        func pop() -> ListNode {
            let top = heap[0].2
            heap[0] = heap[heap.count - 1]
            heap.removeLast()
            var index = 0
            while true {
                let left = 2 * index + 1
                let right = left + 1
                var smallest = index
                if left < heap.count {
                    if heap[left].0 < heap[smallest].0 ||
                        (heap[left].0 == heap[smallest].0 && heap[left].1 < heap[smallest].1) {
                        smallest = left
                    }
                }
                if right < heap.count {
                    if heap[right].0 < heap[smallest].0 ||
                        (heap[right].0 == heap[smallest].0 && heap[right].1 < heap[smallest].1) {
                        smallest = right
                    }
                }
                if smallest == index {
                    break
                }
                heap.swapAt(index, smallest)
                index = smallest
            }
            return top
        }

        for node in lists {
            if let node = node {
                push(node)
            }
        }

        let dummy = ListNode()
        var current: ListNode? = dummy

        while !heap.isEmpty {
            let node = pop()
            current?.next = node
            current = current?.next
            if let next = node.next {
                push(next)
            }
        }

        return dummy.next
    }
}
