// LeetCode 0418 - Sentence Screen Fitting

// https://leetcode.com/problems/sentence-screen-fitting/



object Solution {

  def wordsTyping(sentence: Array[String], rows: Int, cols: Int): Int = {

    var count = 0

    var index = 0

    val total = sentence.length



    for (_ <- 0 until rows) {

      var col = 0

      var done = false



      while (!done) {

        val word = sentence(index)

        val needed = word.length + (if (col > 0) 1 else 0)



        if (col + needed > cols) {

          done = true

        } else {

          if (col > 0) {

            col += 1

          }



          col += word.length

          index = (index + 1) % total



          if (index == 0) {

            count += 1

          }

        }

      }

    }



    count

  }

}
