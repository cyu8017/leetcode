// LeetCode 1656 - Design an Ordered Stream
// https://leetcode.com/problems/design-an-ordered-stream/

class OrderedStream {
    private var a: [String?]
    private var p: Int

    init(_ n: Int) {
        a = Array(repeating: nil, count: n + 1)
        p = 1
    }

    func insert(_ idKey: Int, _ value: String) -> [String] {
        a[idKey] = value
        var out = [String]()
        while p < a.count, let v = a[p] {
            out.append(v)
            p += 1
        }
        return out
    }
}
