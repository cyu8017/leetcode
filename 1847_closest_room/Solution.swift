// LeetCode 1847 - Closest Room
// https://leetcode.com/problems/closest-room/

class Solution {
    func closestRoom(_ rooms: [[Int]], _ queries: [[Int]]) -> [Int] {
        let sortedRooms = rooms.sorted { $0[1] < $1[1] }
        var indexed = queries.enumerated().map { ($0.offset, $0.element[0], $0.element[1]) }
        indexed.sort { $0.2 > $1.2 }
        var availableIds = [Int]()
        var roomIndex = sortedRooms.count - 1
        var answer = Array(repeating: -1, count: queries.count)

        for (queryIndex, preferred, minSize) in indexed {
            while roomIndex >= 0 && sortedRooms[roomIndex][1] >= minSize {
                let roomId = sortedRooms[roomIndex][0]
                var lo = 0, hi = availableIds.count
                while lo < hi {
                    let mid = (lo + hi) / 2
                    if availableIds[mid] < roomId { lo = mid + 1 } else { hi = mid }
                }
                availableIds.insert(roomId, at: lo)
                roomIndex -= 1
            }
            if availableIds.isEmpty { continue }

            var lo = 0, hi = availableIds.count
            while lo < hi {
                let mid = (lo + hi) / 2
                if availableIds[mid] < preferred { lo = mid + 1 } else { hi = mid }
            }
            var bestId = -1
            var bestDist = Int.max
            if lo < availableIds.count {
                let roomId = availableIds[lo]
                let dist = abs(roomId - preferred)
                if dist < bestDist || (dist == bestDist && roomId < bestId) {
                    bestId = roomId
                    bestDist = dist
                }
            }
            if lo > 0 {
                let roomId = availableIds[lo - 1]
                let dist = abs(roomId - preferred)
                if dist < bestDist || (dist == bestDist && roomId < bestId) {
                    bestId = roomId
                }
            }
            answer[queryIndex] = bestId
        }
        return answer
    }
}
