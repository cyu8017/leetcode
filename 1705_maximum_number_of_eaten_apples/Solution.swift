// LeetCode 1705 - Maximum Number of Eaten Apples
// https://leetcode.com/problems/maximum-number-of-eaten-apples/

class Solution {
    func eatenApples(_ apples: [Int], _ days: [Int]) -> Int {
        var heap = [(expire: Int, count: Int)]()

        func push(_ item: (expire: Int, count: Int)) {
            heap.append(item)
            var i = heap.count - 1
            while i > 0 {
                let parent = (i - 1) / 2
                if heap[parent].expire <= heap[i].expire {
                    break
                }
                heap.swapAt(parent, i)
                i = parent
            }
        }

        func pop() -> (expire: Int, count: Int) {
            let top = heap[0]
            heap[0] = heap[heap.count - 1]
            heap.removeLast()
            var i = 0
            while true {
                var smallest = i
                let left = 2 * i + 1
                let right = 2 * i + 2
                if left < heap.count && heap[left].expire < heap[smallest].expire {
                    smallest = left
                }
                if right < heap.count && heap[right].expire < heap[smallest].expire {
                    smallest = right
                }
                if smallest == i {
                    break
                }
                heap.swapAt(smallest, i)
                i = smallest
            }
            return top
        }

        let n = apples.count
        var day = 0
        var eaten = 0
        while day < n || !heap.isEmpty {
            if day < n && apples[day] > 0 {
                push((expire: day + days[day], count: apples[day]))
            }
            while !heap.isEmpty && heap[0].expire <= day {
                _ = pop()
            }
            if !heap.isEmpty {
                let top = pop()
                eaten += 1
                if top.count > 1 {
                    push((expire: top.expire, count: top.count - 1))
                }
            }
            day += 1
        }
        return eaten
    }
}
