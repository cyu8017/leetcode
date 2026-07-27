// LeetCode 1670 - Design Front Middle Back Queue
// https://leetcode.com/problems/design-front-middle-back-queue/

class FrontMiddleBackQueue {
    private var l = [Int]()
    private var r = [Int]()

    init() {}

    private func bal() {
        while l.count > r.count + 1 {
            r.insert(l.removeLast(), at: 0)
        }
        while r.count > l.count {
            l.append(r.removeFirst())
        }
    }

    func pushFront(_ val: Int) {
        l.insert(val, at: 0)
        bal()
    }

    func pushMiddle(_ val: Int) {
        if l.count > r.count {
            r.insert(l.removeLast(), at: 0)
        }
        l.append(val)
    }

    func pushBack(_ val: Int) {
        r.append(val)
        bal()
    }

    func popFront() -> Int {
        if l.isEmpty { return -1 }
        let v = l.removeFirst()
        bal()
        return v
    }

    func popMiddle() -> Int {
        if l.isEmpty { return -1 }
        let v = l.removeLast()
        bal()
        return v
    }

    func popBack() -> Int {
        if l.isEmpty { return -1 }
        let v = r.isEmpty ? l.removeLast() : r.removeLast()
        bal()
        return v
    }
}
