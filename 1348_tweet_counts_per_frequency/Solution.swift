// LeetCode 1348 - Tweet Counts Per Frequency
// https://leetcode.com/problems/tweet-counts-per-frequency/

class TweetCounts {
    private var times = [String: [Int]]()

    init() {}

    func recordTweet(_ tweetName: String, _ time: Int) {
        var arr = times[tweetName, default: []]
        let idx = arr.firstIndex { $0 > time } ?? arr.count
        arr.insert(time, at: idx)
        times[tweetName] = arr
    }

    func getTweetCountsPerFrequency(_ freq: String, _ tweetName: String, _ startTime: Int, _ endTime: Int) -> [Int] {
        let size = ["minute": 60, "hour": 3600, "day": 86400][freq]!
        let arr = times[tweetName, default: []]
        var answer = [Int]()
        var start = startTime
        while start <= endTime {
            let end = min(endTime, start + size - 1)
            let left = arr.firstIndex { $0 >= start } ?? arr.count
            let right = arr.firstIndex { $0 > end } ?? arr.count
            answer.append(right - left)
            start += size
        }
        return answer
    }
}
