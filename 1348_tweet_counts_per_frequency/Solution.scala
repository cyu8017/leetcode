import scala.collection.mutable

class TweetCounts {
  private val times = mutable.Map.empty[String, mutable.ArrayBuffer[Int]]
  def recordTweet(tweetName: String, time: Int): Unit = {
    val list = times.getOrElseUpdate(tweetName, mutable.ArrayBuffer.empty)
    list.insert(list.indexWhere(_ >= time) match { case -1 => list.length; case i => i }, time)
  }
  def getTweetCountsPerFrequency(freq: String, tweetName: String, startTime: Int, endTime: Int): List[Int] = {
    val size = if (freq == "minute") 60 else if (freq == "hour") 3600 else 86400
    val list = times.getOrElse(tweetName, mutable.ArrayBuffer.empty)
    (startTime to endTime by size).map(start => list.count(time => time >= start && time <= math.min(endTime, start + size - 1))).toList
  }
}
