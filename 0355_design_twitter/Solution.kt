// LeetCode 0355 - Design Twitter

// https://leetcode.com/problems/design-twitter/



import java.util.PriorityQueue



class Twitter {

    private var time = 0

    private val tweets = mutableMapOf<Int, MutableList<IntArray>>()

    private val following = mutableMapOf<Int, MutableSet<Int>>()



    fun postTweet(userId: Int, tweetId: Int) {

        time++

        tweets.computeIfAbsent(userId) { mutableListOf() }

            .add(intArrayOf(time, tweetId))

    }



    fun getNewsFeed(userId: Int): List<Int> {

        val heap = PriorityQueue<IntArray>(compareByDescending { it[0] })

        val users = following.getOrDefault(userId, mutableSetOf()).toMutableSet()

        users.add(userId)



        for (uid in users) {

            val userTweets = tweets[uid] ?: continue

            val start = maxOf(0, userTweets.size - 10)

            for (index in start until userTweets.size) {

                heap.offer(userTweets[index])

            }

        }



        val feed = mutableListOf<Int>()

        while (heap.isNotEmpty() && feed.size < 10) {

            feed.add(heap.poll()[1])

        }



        return feed

    }



    fun follow(followerId: Int, followeeId: Int) {

        following.computeIfAbsent(followerId) { mutableSetOf() }.add(followeeId)

    }



    fun unfollow(followerId: Int, followeeId: Int) {

        following[followerId]?.remove(followeeId)

    }

}
