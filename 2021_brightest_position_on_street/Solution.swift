// LeetCode 2021 - Brightest Position on Street
// https://leetcode.com/problems/brightest-position-on-street/

class Solution {
    func brightestPosition(_ lights: [[Int]]) -> Int {
        var events = [(Int, Int)]()
        for light in lights {
            let pos = light[0], r = light[1]
            events.append((pos - r, 1))
            events.append((pos + r + 1, -1))
        }
        events.sort {
            if $0.0 != $1.0 { return $0.0 < $1.0 }
            return $0.1 > $1.1
        }
        var best = 0, cur = 0, ans = 0
        for e in events {
            cur += e.1
            if cur > best {
                best = cur
                ans = e.0
            }
        }
        return ans
    }
}
