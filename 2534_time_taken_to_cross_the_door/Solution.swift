// LeetCode 2534 - Time Taken to Cross the Door
// https://leetcode.com/problems/time-taken-to-cross-the-door/

class Solution {
    func timeTaken(_ arrival: [Int], _ state: [Int]) -> [Int] {
        let n = arrival.count
        var ans = [Int](repeating: 0, count: n)
        var enter = [Int]()
        var exitq = [Int]()
        var ei = 0, xi = 0
        var i = 0, t = 0, prev = 1
        while i < n || ei < enter.count || xi < exitq.count {
            while i < n && arrival[i] <= t {
                if state[i] == 0 { enter.append(i) } else { exitq.append(i) }
                i += 1
            }
            if ei == enter.count && xi == exitq.count {
                if i < n {
                    t = arrival[i]
                    prev = 1
                }
                continue
            }
            if prev == 1 {
                if xi < exitq.count {
                    ans[exitq[xi]] = t
                    xi += 1
                    prev = 1
                } else {
                    ans[enter[ei]] = t
                    ei += 1
                    prev = 0
                }
            } else {
                if ei < enter.count {
                    ans[enter[ei]] = t
                    ei += 1
                    prev = 0
                } else {
                    ans[exitq[xi]] = t
                    xi += 1
                    prev = 1
                }
            }
            t += 1
        }
        return ans
    }
}
