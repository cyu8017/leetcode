// LeetCode 1942 - The Number of the Smallest Unoccupied Chair
// https://leetcode.com/problems/the-number-of-the-smallest-unoccupied-chair/

class Solution {
    func smallestChair(_ times: [[Int]], _ targetFriend: Int) -> Int {
        let order = times.indices.sorted { times[$0][0] < times[$1][0] }
        var free: [Int] = []
        var nextChair = 0
        var leaving: [(Int, Int)] = [] // leave, chair

        func pushFree(_ x: Int) {
            free.append(x)
            var i = free.count - 1
            while i > 0 {
                let p = (i - 1) / 2
                if free[p] <= free[i] { break }
                free.swapAt(p, i); i = p
            }
        }
        func popFree() -> Int {
            let top = free[0]
            let last = free.removeLast()
            if !free.isEmpty {
                free[0] = last
                var i = 0
                while true {
                    var s = i
                    let l = 2 * i + 1, r = 2 * i + 2
                    if l < free.count && free[l] < free[s] { s = l }
                    if r < free.count && free[r] < free[s] { s = r }
                    if s == i { break }
                    free.swapAt(i, s); i = s
                }
            }
            return top
        }
        func pushLeaving(_ item: (Int, Int)) {
            leaving.append(item)
            var i = leaving.count - 1
            while i > 0 {
                let p = (i - 1) / 2
                if leaving[p].0 <= leaving[i].0 { break }
                leaving.swapAt(p, i); i = p
            }
        }
        func popLeaving() -> (Int, Int) {
            let top = leaving[0]
            let last = leaving.removeLast()
            if !leaving.isEmpty {
                leaving[0] = last
                var i = 0
                while true {
                    var s = i
                    let l = 2 * i + 1, r = 2 * i + 2
                    if l < leaving.count && leaving[l].0 < leaving[s].0 { s = l }
                    if r < leaving.count && leaving[r].0 < leaving[s].0 { s = r }
                    if s == i { break }
                    leaving.swapAt(i, s); i = s
                }
            }
            return top
        }

        for i in order {
            let arr = times[i][0], leave = times[i][1]
            while !leaving.isEmpty && leaving[0].0 <= arr {
                pushFree(popLeaving().1)
            }
            let chair: Int
            if !free.isEmpty {
                chair = popFree()
            } else {
                chair = nextChair
                nextChair += 1
            }
            if i == targetFriend { return chair }
            pushLeaving((leave, chair))
        }
        return -1
    }
}
