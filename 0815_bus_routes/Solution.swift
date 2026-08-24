// LeetCode 0815 - Bus Routes
// https://leetcode.com/problems/bus-routes/

class Solution {
    func numBusesToDestination(_ routes: [[Int]], _ source: Int, _ target: Int) -> Int {
        if source == target { return 0 }
        var stopToBuses = [Int: [Int]]()
        for bus in 0..<routes.count {
            for stop in routes[bus] {
                stopToBuses[stop, default: []].append(bus)
            }
        }
        var queue = [(source, 0)]
        var seenStops: Set<Int> = [source]
        var seenBuses = Set<Int>()
        var qi = 0
        while qi < queue.count {
            let (stop, busesTaken) = queue[qi]
            qi += 1
            for bus in stopToBuses[stop, default: []] {
                if !seenBuses.insert(bus).inserted { continue }
                for nxt in routes[bus] {
                    if nxt == target { return busesTaken + 1 }
                    if seenStops.insert(nxt).inserted {
                        queue.append((nxt, busesTaken + 1))
                    }
                }
            }
        }
        return -1
    }
}
