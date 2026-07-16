// LeetCode 0341 - Flatten Nested List Iterator
// https://leetcode.com/problems/flatten-nested-list-iterator/

class NestedInteger {
    private var integer: Int?
    private var list: [NestedInteger] = []

    init(_ value: Int) {
        self.integer = value
    }

    init() {}

    func isInteger() -> Bool {
        integer != nil
    }

    func getInteger() -> Int {
        integer ?? 0
    }

    func getList() -> [NestedInteger] {
        list
    }

    func add(_ item: NestedInteger) {
        list.append(item)
    }
}

class NestedIterator {
    private var stack: [(NestedInteger, Int)] = []

    init(_ nestedList: [NestedInteger]) {
        for index in stride(from: nestedList.count - 1, through: 0, by: -1) {
            stack.append((nestedList[index], 0))
        }
    }

    func next() -> Int {
        prepareNext()
        let current = stack.removeLast().0
        return current.getInteger()
    }

    func hasNext() -> Bool {
        prepareNext()
        return !stack.isEmpty
    }

    private func prepareNext() {
        while let last = stack.last {
            let current = last.0
            let index = last.1
            if current.isInteger() {
                return
            }

            let nested = current.getList()
            if index >= nested.count {
                stack.removeLast()
                continue
            }

            stack[stack.count - 1] = (current, index + 1)
            stack.append((nested[index], 0))
        }
    }
}
