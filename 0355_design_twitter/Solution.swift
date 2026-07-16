// LeetCode 0355 - Design Twitter
// https://leetcode.com/problems/design-twitter/

class Twitter {
    private var time = 0
    private var tweets: [Int: [(Int, Int)]] = [:]
    private var following: [Int: Set<Int>] = [:]

    init() {
    }

    func postTweet(_ userId: Int, _ tweetId: Int) {
        time += 1
        tweets[userId, default: []].append((time, tweetId))
    }

    func getNewsFeed(_ userId: Int) -> [Int] {
        var users = following[userId, default: []]
        users.insert(userId)

        var candidates: [(Int, Int)] = []
        for uid in users {
            let recent = tweets[uid, default: []].suffix(10)
            candidates.append(contentsOf: recent)
        }

        candidates.sort { $0.0 > $1.0 }
        return Array(candidates.prefix(10).map { $0.1 })
    }

    func follow(_ followerId: Int, _ followeeId: Int) {
        following[followerId, default: []].insert(followeeId)
    }

    func unfollow(_ followerId: Int, _ followeeId: Int) {
        following[followerId]?.remove(followeeId)
    }
}
