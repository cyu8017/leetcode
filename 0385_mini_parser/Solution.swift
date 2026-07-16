// LeetCode 0385 - Mini Parser
// https://leetcode.com/problems/mini-parser/

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

class Solution {
    func deserialize(_ s: String) -> NestedInteger {
        let chars = Array(s)
        if chars[0] != "[" {
            return NestedInteger(Int(s) ?? 0)
        }

        var stack: [NestedInteger] = []
        var current: NestedInteger? = nil
        var index = 0
        var negative = false
        var number = 0
        var hasNumber = false

        while index < chars.count {
            let char = chars[index]
            if char == "[" {
                let item = NestedInteger()
                if let parent = current {
                    stack.append(parent)
                }
                current = item
            } else if char == "-" {
                negative = true
            } else if char >= "0" && char <= "9" {
                number = number * 10 + Int(String(char))!
                hasNumber = true
            } else if char == "," || char == "]" {
                if hasNumber, let current {
                    let value = negative ? -number : number
                    current.add(NestedInteger(value))
                    number = 0
                    negative = false
                    hasNumber = false
                }
                if char == "]", let current {
                    if stack.isEmpty {
                        return current
                    }
                    let parent = stack.removeLast()
                    parent.add(current)
                    current = parent
                }
            }
            index += 1
        }

        return current ?? NestedInteger()
    }
}
