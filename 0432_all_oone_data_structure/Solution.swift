// LeetCode 0432 - All O`one` Data Structure
// https://leetcode.com/problems/all-oone-data-structure/

class CountNode {
    let count: Int
    var keys: Set<String> = []
    var previous: CountNode?
    var next: CountNode?

    init(_ count: Int = 0) {
        self.count = count
    }
}

class AllOne {
    private let head = CountNode()
    private let tail = CountNode()
    private var keyNodes: [String: CountNode] = [:]

    init() {
        head.next = tail
        tail.previous = head
    }

    func inc(_ key: String) {
        if let bucket = keyNodes[key] {
            bucket.keys.remove(key)
            let nextBucket = ensureCountNode(bucket.count + 1, after: bucket)
            nextBucket.keys.insert(key)
            keyNodes[key] = nextBucket
            if bucket.keys.isEmpty {
                remove(bucket)
            }
            return
        }

        let bucket = ensureCountNode(1, after: head)
        bucket.keys.insert(key)
        keyNodes[key] = bucket
    }

    func dec(_ key: String) {
        guard let bucket = keyNodes[key] else {
            return
        }
        bucket.keys.remove(key)
        if bucket.count == 1 {
            keyNodes[key] = nil
        } else {
            let previousBucket = ensureCountNode(bucket.count - 1, after: head)
            previousBucket.keys.insert(key)
            keyNodes[key] = previousBucket
        }
        if bucket.keys.isEmpty {
            remove(bucket)
        }
    }

    func getMaxKey() -> String {
        guard let bucket = tail.previous, bucket !== head else {
            return ""
        }
        return bucket.keys.first ?? ""
    }

    func getMinKey() -> String {
        guard let bucket = head.next, bucket !== tail else {
            return ""
        }
        return bucket.keys.first ?? ""
    }

    private func insertAfter(_ anchor: CountNode, _ node: CountNode) {
        node.previous = anchor
        node.next = anchor.next
        anchor.next?.previous = node
        anchor.next = node
    }

    private func remove(_ node: CountNode) {
        node.previous?.next = node.next
        node.next?.previous = node.previous
    }

    private func ensureCountNode(_ count: Int, after: CountNode) -> CountNode {
        var current = after.next
        while let currentNode = current, currentNode !== tail {
            if currentNode.count >= count {
                if currentNode.count == count {
                    return currentNode
                }
                let bucket = CountNode(count)
                insertAfter(currentNode.previous!, bucket)
                return bucket
            }
            current = currentNode.next
        }
        let bucket = CountNode(count)
        insertAfter(tail.previous!, bucket)
        return bucket
    }
}
