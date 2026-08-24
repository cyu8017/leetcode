// LeetCode 2296 - Design a Text Editor
// https://leetcode.com/problems/design-a-text-editor/

class TextEditor {
    private var left: [Character] = []
    private var right: [Character] = []

    init() {}

    func addText(_ text: String) {
        left.append(contentsOf: text)
    }

    func deleteText(_ k: Int) -> Int {
        var k = k, deleted = 0
        while k > 0 && !left.isEmpty {
            left.removeLast()
            k -= 1
            deleted += 1
        }
        return deleted
    }

    func cursorLeft(_ k: Int) -> String {
        var k = k
        while k > 0 && !left.isEmpty {
            right.append(left.removeLast())
            k -= 1
        }
        return suffix()
    }

    func cursorRight(_ k: Int) -> String {
        var k = k
        while k > 0 && !right.isEmpty {
            left.append(right.removeLast())
            k -= 1
        }
        return suffix()
    }

    private func suffix() -> String {
        let start = max(0, left.count - 10)
        return String(left[start...])
    }
}
