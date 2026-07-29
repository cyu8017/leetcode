// LeetCode 1024 - Video Stitching
// https://leetcode.com/problems/video-stitching/

object Solution {
  def videoStitching(clips: Array[Array[Int]], time: Int): Int = {
    val furthest = Array.fill(time + 1)(0)
    for (clip <- clips) {
      val start = clip(0)
      val end = clip(1)
      if (start <= time) furthest(start) = math.max(furthest(start), end)
    }
    var ans = 0
    var reach = 0
    var nextReach = 0
    for (i <- 0 until time) {
      nextReach = math.max(nextReach, furthest(i))
      if (i == reach) {
        if (nextReach <= i) return -1
        ans += 1
        reach = nextReach
      }
    }
    ans
  }
}
