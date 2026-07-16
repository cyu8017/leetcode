// LeetCode 0355 - Design Twitter

// https://leetcode.com/problems/design-twitter/



import scala.collection.mutable



class Twitter {

  private var time = 0

  private val tweets = mutable.Map.empty[Int, mutable.ArrayBuffer[Array[Int]]]

  private val following = mutable.Map.empty[Int, mutable.Set[Int]]



  def postTweet(userId: Int, tweetId: Int): Unit = {

    time += 1

    tweets.getOrElseUpdate(userId, mutable.ArrayBuffer.empty) += Array(time, tweetId)

  }



  def getNewsFeed(userId: Int): List[Int] = {

    implicit val ordering: Ordering[Array[Int]] = Ordering.by((item: Array[Int]) => -item(0))

    val heap = mutable.PriorityQueue.empty[Array[Int]]

    val users = following.getOrElse(userId, mutable.Set.empty[Int]).toSet + userId



    for (uid <- users) {

      tweets.get(uid).foreach { userTweets =>

        val start = math.max(0, userTweets.size - 10)

        for (index <- start until userTweets.size) {

          heap.enqueue(userTweets(index))

        }

      }

    }



    val feed = mutable.ArrayBuffer.empty[Int]

    while (heap.nonEmpty && feed.size < 10) {

      feed += heap.dequeue()(1)

    }



    feed.toList

  }



  def follow(followerId: Int, followeeId: Int): Unit = {

    following.getOrElseUpdate(followerId, mutable.Set.empty) += followeeId

  }



  def unfollow(followerId: Int, followeeId: Int): Unit = {

    following.get(followerId).foreach(_.remove(followeeId))

  }

}
