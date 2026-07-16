class Node {
    let key: Int
    var value: Int
    var previous: Node?
    var next: Node?

    init(_ key: Int = 0, _ value: Int = 0) {
        self.key = key
        self.value = value
    }
}

class LRUCache {
    private let capacity: Int
    private var cache = [Int: Node]()
    private let head = Node()
    private let tail = Node()

    init(_ capacity: Int) {
        self.capacity = capacity
        head.next = tail
        tail.previous = head
    }

    private func remove(_ node: Node) {
        node.previous?.next = node.next
        node.next?.previous = node.previous
    }

    private func addToFront(_ node: Node) {
        node.previous = head
        node.next = head.next
        head.next?.previous = node
        head.next = node
    }

    func get(_ key: Int) -> Int {
        guard let node = cache[key] else { return -1 }
        remove(node)
        addToFront(node)
        return node.value
    }

    func put(_ key: Int, _ value: Int) {
        if let node = cache[key] {
            node.value = value
            remove(node)
            addToFront(node)
            return
        }
        if cache.count == capacity, let leastRecent = tail.previous {
            remove(leastRecent)
            cache[leastRecent.key] = nil
        }
        let node = Node(key, value)
        cache[key] = node
        addToFront(node)
    }
}