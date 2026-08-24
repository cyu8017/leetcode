// LeetCode 2502 - Design Memory Allocator
// https://leetcode.com/problems/design-memory-allocator/

class Allocator {
    private var mem: [Int]

    init(_ n: Int) {
        mem = [Int](repeating: 0, count: n)
    }

    func allocate(_ size: Int, _ mID: Int) -> Int {
        var freeCnt = 0
        for i in 0..<mem.count {
            if mem[i] == 0 {
                freeCnt += 1
                if freeCnt == size {
                    let start = i - size + 1
                    for j in start...i { mem[j] = mID }
                    return start
                }
            } else {
                freeCnt = 0
            }
        }
        return -1
    }

    func freeMemory(_ mID: Int) -> Int {
        var cnt = 0
        for i in 0..<mem.count {
            if mem[i] == mID {
                mem[i] = 0
                cnt += 1
            }
        }
        return cnt
    }
}
