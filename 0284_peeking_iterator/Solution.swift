// LeetCode 0284 - Peeking Iterator
// https://leetcode.com/problems/peeking-iterator/

protocol NumberIterator {
    func next() -> Int
    func hasNext() -> Bool
}

class ListIterator: NumberIterator {
    private var values: [Int]
    private var index: Int

    init(_ values: [Int]) {
        self.values = values
        self.index = 0
    }

    func next() -> Int {
        let value = values[index]
        index += 1
        return value
    }

    func hasNext() -> Bool {
        index < values.count
    }
}

class PeekingIterator {
    private var iterator: NumberIterator
    private var peeked: Int?
    private var hasPeeked: Bool

    init(_ iterator: NumberIterator) {
        self.iterator = iterator
        self.peeked = nil
        self.hasPeeked = false
    }

    func peek() -> Int {
        if !hasPeeked {
            peeked = iterator.next()
            hasPeeked = true
        }
        return peeked!
    }

    func next() -> Int {
        if hasPeeked {
            let result = peeked!
            peeked = nil
            hasPeeked = false
            return result
        }
        return iterator.next()
    }

    func hasNext() -> Bool {
        hasPeeked || iterator.hasNext()
    }
}
