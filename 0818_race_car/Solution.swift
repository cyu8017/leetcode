// LeetCode 0818 - Race Car
// https://leetcode.com/problems/race-car/

class Solution {
    func racecar(_ target: Int) -> Int {
        var queue = [(0, 1, 0)]
        var seen: Set<Int> = [key(0, 1)]
        var qi = 0
        while qi < queue.count {
            let (pos, speed, steps) = queue[qi]
            qi += 1
            if pos == target { return steps }
            let nxtPos = pos + speed
            let nxtSpeed = speed * 2
            let k1 = key(nxtPos, nxtSpeed)
            if !seen.contains(k1) && abs(nxtPos) < target * 2 {
                seen.insert(k1)
                queue.append((nxtPos, nxtSpeed, steps + 1))
            }
            let revSpeed = speed > 0 ? -1 : 1
            let k2 = key(pos, revSpeed)
            if seen.insert(k2).inserted {
                queue.append((pos, revSpeed, steps + 1))
            }
        }
        return -1
    }

    private func key(_ pos: Int, _ speed: Int) -> Int {
        return (pos << 20) ^ (speed & 0xfffff)
    }
}
