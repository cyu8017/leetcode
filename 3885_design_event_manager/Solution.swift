// LeetCode 3885 - Design Event Manager
// https://leetcode.com/problems/design-event-manager/

class EventManager {
    private var sl = [(Int, Int)]()
    private var d = [Int: Int]()

    init(_ events: [[Int]]) {
        for e in events {
            sl.append((-e[1], e[0]))
            d[e[0]] = e[1]
        }
        sl.sort { $0.0 != $1.0 ? $0.0 < $1.0 : $0.1 < $1.1 }
    }

    func updatePriority(_ eventId: Int, _ newPriority: Int) {
        let old = d[eventId]!
        if let i = sl.firstIndex(where: { $0.0 == -old && $0.1 == eventId }) {
            sl.remove(at: i)
        }
        sl.append((-newPriority, eventId))
        sl.sort { $0.0 != $1.0 ? $0.0 < $1.0 : $0.1 < $1.1 }
        d[eventId] = newPriority
    }

    func pollHighest() -> Int {
        if sl.isEmpty { return -1 }
        let top = sl.removeFirst()
        d.removeValue(forKey: top.1)
        return top.1
    }
}
