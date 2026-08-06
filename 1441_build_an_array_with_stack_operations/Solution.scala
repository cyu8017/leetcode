import scala.collection.mutable
object Solution {
  def buildArray(target: Array[Int], n: Int): List[String] = {
    val answer = mutable.ListBuffer.empty[String]; var current = 1
    for (value <- target) {
      while (current < value) { answer += "Push"; answer += "Pop"; current += 1 }
      answer += "Push"; current += 1
    }
    answer.toList
  }
}
