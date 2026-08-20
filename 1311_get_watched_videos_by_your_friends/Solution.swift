// LeetCode 1311 - Get Watched Videos by Your Friends
// https://leetcode.com/problems/get-watched-videos-by-your-friends/

class Solution {
    func watchedVideosByFriends(_ watchedVideos: [[String]], _ friends: [[Int]], _ id: Int, _ level: Int) -> [String] {
        var queue = [(id, 0)], seen: Set<Int> = [id], people = [Int](), qi = 0
        while qi < queue.count {
            let (person, distance) = queue[qi]; qi += 1
            if distance == level { people.append(person); continue }
            for friend in friends[person] where !seen.contains(friend) {
                seen.insert(friend); queue.append((friend, distance + 1))
            }
        }
        var counts = [String: Int]()
        for person in people {
            for video in watchedVideos[person] { counts[video, default: 0] += 1 }
        }
        return counts.keys.sorted { (counts[$0]!, $0) < (counts[$1]!, $1) }
    }
}
