// LeetCode 0630 - Course Schedule III
// https://leetcode.com/problems/course-schedule-iii/

class Solution {
    func scheduleCourse(_ courses: [[Int]]) -> Int {
        let courses = courses.sorted { $0[1] < $1[1] }
        var heap = [Int]()
        var time = 0
        func heapPush(_ val: Int) {
            heap.append(val)
            var i = heap.count - 1
            while i > 0 {
                let p = (i - 1) / 2
                if heap[p] >= heap[i] { break }
                heap.swapAt(p, i)
                i = p
            }
        }
        func heapPop() -> Int {
            let top = heap[0]
            let last = heap.removeLast()
            if !heap.isEmpty {
                heap[0] = last
                var i = 0
                while true {
                    var best = i
                    let l = 2 * i + 1, r = 2 * i + 2
                    if l < heap.count && heap[l] > heap[best] { best = l }
                    if r < heap.count && heap[r] > heap[best] { best = r }
                    if best == i { break }
                    heap.swapAt(i, best)
                    i = best
                }
            }
            return top
        }
        for course in courses {
            let duration = course[0]
            let lastDay = course[1]
            if time + duration <= lastDay {
                heapPush(duration)
                time += duration
            } else if !heap.isEmpty && heap[0] > duration {
                time += duration - heapPop()
                heapPush(duration)
            }
        }
        return heap.count
    }
}
