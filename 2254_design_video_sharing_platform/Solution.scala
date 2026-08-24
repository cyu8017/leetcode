// LeetCode 2254 - Design Video Sharing Platform
// https://leetcode.com/problems/design-video-sharing-platform/

class VideoSharingPlatform() {
  private var nextID = 0
  private val free = scala.collection.mutable.PriorityQueue.empty[Int](Ordering[Int].reverse)
  private val videos = scala.collection.mutable.HashMap.empty[Int, String]
  private val views = scala.collection.mutable.HashMap.empty[Int, Int]
  private val likes = scala.collection.mutable.HashMap.empty[Int, Int]
  private val dislikes = scala.collection.mutable.HashMap.empty[Int, Int]

  def upload(video: String): Int = {
    val id = if (free.isEmpty) {
      val v = nextID
      nextID += 1
      v
    } else free.dequeue()
    videos(id) = video
    views(id) = 0
    likes(id) = 0
    dislikes(id) = 0
    id
  }

  def remove(videoId: Int): Unit = {
    if (!videos.contains(videoId)) return
    videos.remove(videoId)
    views.remove(videoId)
    likes.remove(videoId)
    dislikes.remove(videoId)
    free.enqueue(videoId)
  }

  def watch(videoId: Int, startMinute: Int, endMinute0: Int): String = {
    val v = videos.getOrElse(videoId, null)
    if (v == null) return "-1"
    views(videoId) = views(videoId) + 1
    if (startMinute >= v.length) return ""
    val endMinute = math.min(endMinute0, v.length - 1)
    v.substring(startMinute, endMinute + 1)
  }

  def like(videoId: Int): Unit = {
    if (videos.contains(videoId)) likes(videoId) = likes(videoId) + 1
  }

  def dislike(videoId: Int): Unit = {
    if (videos.contains(videoId)) dislikes(videoId) = dislikes(videoId) + 1
  }

  def getLikesAndDislikes(videoId: Int): Array[Int] = {
    if (!videos.contains(videoId)) return Array(-1)
    Array(likes(videoId), dislikes(videoId))
  }

  def getViews(videoId: Int): Int = {
    if (!videos.contains(videoId)) return -1
    views(videoId)
  }
}
