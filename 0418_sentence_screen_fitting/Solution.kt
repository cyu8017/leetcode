// LeetCode 0418 - Sentence Screen Fitting

// https://leetcode.com/problems/sentence-screen-fitting/



class Solution {

    fun wordsTyping(sentence: Array<String>, rows: Int, cols: Int): Int {

        var count = 0

        var index = 0

        val total = sentence.size



        repeat(rows) {

            var col = 0



            while (true) {

                val word = sentence[index]

                val needed = word.length + if (col > 0) 1 else 0



                if (col + needed > cols) {

                    break

                }



                if (col > 0) {

                    col++

                }



                col += word.length

                index = (index + 1) % total



                if (index == 0) {

                    count++

                }

            }

        }



        return count

    }

}
