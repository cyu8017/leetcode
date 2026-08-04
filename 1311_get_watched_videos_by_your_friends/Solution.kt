// LeetCode 1311 - Get Watched Videos by Your Friends
// https://leetcode.com/problems/get-watched-videos-by-your-friends/

class Solution {
    fun watchedVideosByFriends(
        watchedVideos: List<List<String>>,
        friends: Array<IntArray>,
        id: Int,
        level: Int
    ): List<String> {
        val queue = ArrayDeque<Pair<Int, Int>>()
        val seen = mutableSetOf(id)
        queue.add(id to 0)
        val people = mutableListOf<Int>()
        while (queue.isNotEmpty()) {
            val (person, distance) = queue.removeFirst()
            if (distance == level) {
                people.add(person)
                continue
            }
            for (friend in friends[person]) {
                if (friend !in seen) {
                    seen.add(friend)
                    queue.add(friend to distance + 1)
                }
            }
        }
        val counts = mutableMapOf<String, Int>()
        for (person in people) {
            for (video in watchedVideos[person]) {
                counts[video] = counts.getOrDefault(video, 0) + 1
            }
        }
        return counts.keys.sortedWith(compareBy({ counts[it]!! }, { it }))
    }
}
