// LeetCode 2166 - Design Bitset
// https://leetcode.com/problems/design-bitset/

class Bitset {
    private var bits: [UInt8]
    private var ones = 0
    private var flipped = false
    private let size: Int

    init(_ size: Int) {
        self.size = size
        bits = [UInt8](repeating: 0, count: size)
    }

    func fix(_ idx: Int) {
        let target: UInt8 = flipped ? 0 : 1
        if bits[idx] != target {
            bits[idx] = target
            ones += flipped ? -1 : 1
        }
    }

    func unfix(_ idx: Int) {
        let target: UInt8 = flipped ? 1 : 0
        if bits[idx] != target {
            bits[idx] = target
            ones += flipped ? 1 : -1
        }
    }

    func flip() {
        flipped.toggle()
        ones = size - ones
    }

    func all() -> Bool { ones == size }
    func one() -> Bool { ones > 0 }
    func count() -> Int { ones }

    func toString() -> String {
        var b = [Character]()
        for i in 0..<size {
            var v = bits[i]
            if flipped { v ^= 1 }
            b.append(v == 0 ? "0" : "1")
        }
        return String(b)
    }
}
