// LeetCode 2254 - Design Video Sharing Platform
// https://leetcode.com/problems/design-video-sharing-platform/

private struct MinHeap {
    private var data: [Int] = []
    var isEmpty: Bool { data.isEmpty }
    mutating func push(_ x: Int) {
        data.append(x)
        siftUp(data.count - 1)
    }
    mutating func pop() -> Int {
        let top = data[0]
        let last = data.removeLast()
        if !data.isEmpty { data[0] = last; siftDown(0) }
        return top
    }
    private mutating func siftUp(_ i: Int) {
        var idx = i
        while idx > 0 {
            let p = (idx - 1) / 2
            if data[p] <= data[idx] { break }
            data.swapAt(p, idx)
            idx = p
        }
    }
    private mutating func siftDown(_ i: Int) {
        var idx = i
        while true {
            var smallest = idx
            let l = idx * 2 + 1, r = idx * 2 + 2
            if l < data.count && data[l] < data[smallest] { smallest = l }
            if r < data.count && data[r] < data[smallest] { smallest = r }
            if smallest == idx { break }
            data.swapAt(smallest, idx)
            idx = smallest
        }
    }
}

class VideoSharingPlatform {
    private var nextID = 0
    private var free = MinHeap()
    private var videos: [Int: String] = [:]
    private var views: [Int: Int] = [:]
    private var likes: [Int: Int] = [:]
    private var dislikes: [Int: Int] = [:]

    init() {}

    func upload(_ video: String) -> Int {
        let id: Int
        if free.isEmpty {
            id = nextID
            nextID += 1
        } else {
            id = free.pop()
        }
        videos[id] = video
        views[id] = 0
        likes[id] = 0
        dislikes[id] = 0
        return id
    }

    func remove(_ videoId: Int) {
        guard videos[videoId] != nil else { return }
        videos.removeValue(forKey: videoId)
        views.removeValue(forKey: videoId)
        likes.removeValue(forKey: videoId)
        dislikes.removeValue(forKey: videoId)
        free.push(videoId)
    }

    func watch(_ videoId: Int, _ startMinute: Int, _ endMinute: Int) -> String {
        guard let v = videos[videoId] else { return "-1" }
        views[videoId, default: 0] += 1
        if startMinute >= v.count { return "" }
        let end = min(endMinute, v.count - 1)
        let arr = Array(v)
        return String(arr[startMinute...end])
    }

    func like(_ videoId: Int) {
        if videos[videoId] != nil { likes[videoId, default: 0] += 1 }
    }

    func dislike(_ videoId: Int) {
        if videos[videoId] != nil { dislikes[videoId, default: 0] += 1 }
    }

    func getLikesAndDislikes(_ videoId: Int) -> [Int] {
        guard videos[videoId] != nil else { return [-1] }
        return [likes[videoId]!, dislikes[videoId]!]
    }

    func getViews(_ videoId: Int) -> Int {
        guard videos[videoId] != nil else { return -1 }
        return views[videoId]!
    }
}
