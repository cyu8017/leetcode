// LeetCode 1286 - Iterator for Combination
// https://leetcode.com/problems/iterator-for-combination/

class CombinationIterator {
    private var items: [String] = []
    private var index = 0

    init(_ characters: String, _ combinationLength: Int) {
        let chars = Array(characters)
        var path = [Character](repeating: " ", count: combinationLength)
        func build(_ start: Int, _ depth: Int) {
            if depth == combinationLength {
                items.append(String(path))
                return
            }
            for i in start..<chars.count {
                path[depth] = chars[i]
                build(i + 1, depth + 1)
            }
        }
        build(0, 0)
    }

    func next() -> String {
        let v = items[index]
        index += 1
        return v
    }

    func hasNext() -> Bool {
        index < items.count
    }
}
