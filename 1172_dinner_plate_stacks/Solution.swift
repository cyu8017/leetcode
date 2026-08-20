// LeetCode 1172 - Dinner Plate Stacks
// https://leetcode.com/problems/dinner-plate-stacks/

class DinnerPlates {
    private let capacity: Int
    private var stacks: [[Int]] = []
    private var available: [Int] = []

    init(_ capacity: Int) {
        self.capacity = capacity
    }

    func push(_ val: Int) {
        while !available.isEmpty && (available[0] >= stacks.count || stacks[available[0]].count == capacity) {
            available.removeFirst()
        }
        if available.isEmpty {
            stacks.append([])
            available.append(stacks.count - 1)
        }
        let i = available[0]
        stacks[i].append(val)
        if stacks[i].count == capacity {
            available.removeFirst()
        }
    }

    func pop() -> Int {
        while !stacks.isEmpty && stacks[stacks.count - 1].isEmpty {
            stacks.removeLast()
        }
        if stacks.isEmpty { return -1 }
        return popAtStack(stacks.count - 1)
    }

    func popAtStack(_ index: Int) -> Int {
        if index < 0 || index >= stacks.count || stacks[index].isEmpty { return -1 }
        let v = stacks[index].removeLast()
        available.append(index)
        available.sort()
        return v
    }
}
