// LeetCode 0358 - Rearrange String k Distance Apart

// https://leetcode.com/problems/rearrange-string-k-distance-apart/



import scala.collection.mutable



object Solution {

  def rearrangeString(s: String, k: Int): String = {

    val counts = mutable.Map.empty[Char, Int]

    for (ch <- s) {

      counts(ch) = counts.getOrElse(ch, 0) + 1

    }



    var maxFreq = 0

    var maxFreqChars = 0

    for (count <- counts.values) {

      if (count > maxFreq) {

        maxFreq = count

        maxFreqChars = 1

      } else if (count == maxFreq) {

        maxFreqChars += 1

      }

    }



    if ((s.length - maxFreqChars) < (maxFreq - 1) * (k - 1)) {

      ""

    } else {

      implicit val ordering: Ordering[(Int, Char)] =

        Ordering.by((item: (Int, Char)) => item._1).orElse(Ordering.by(_._2))

      val heap = mutable.PriorityQueue.from(counts.map { case (ch, count) => (-count, ch) })

      val queue = mutable.Queue.empty[(Int, Char, Int)]

      val result = new StringBuilder

      var index = 0



      while (heap.nonEmpty || queue.nonEmpty) {

        while (queue.nonEmpty && queue.head._3 <= index) {

          val (count, ch, _) = queue.dequeue()

          heap.enqueue((count, ch))

        }



        if (heap.isEmpty) {

          return ""

        }



        val (count, ch) = heap.dequeue()

        result.append(ch)

        if (count + 1 < 0) {

          queue.enqueue((count + 1, ch, index + k))

        }

        index += 1

      }



      result.toString()

    }

  }

}
