// LeetCode 0604 - Design Compressed String Iterator
// https://leetcode.com/problems/design-compressed-string-iterator/

class StringIterator {
    private var chars = [Character]()
    private var counts = [Int]()
    private var index = 0

    init(_ compressedString: String) {
        let arr = Array(compressedString)
        var i = 0
        while i < arr.count {
            let ch = arr[i]
            i += 1
            var j = i
            while j < arr.count && arr[j] >= "0" && arr[j] <= "9" { j += 1 }
            chars.append(ch)
            counts.append(Int(String(arr[i..<j]))!)
            i = j
        }
    }

    func next() -> Character {
        if !hasNext() { return " " }
        let ch = chars[index]
        counts[index] -= 1
        if counts[index] == 0 { index += 1 }
        return ch
    }

    func hasNext() -> Bool {
        index < chars.count
    }
}
