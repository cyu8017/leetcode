// LeetCode 0358 - Rearrange String k Distance Apart

// https://leetcode.com/problems/rearrange-string-k-distance-apart/



import java.util.PriorityQueue



class Solution {

    fun rearrangeString(s: String, k: Int): String {

        val counts = mutableMapOf<Char, Int>()

        for (ch in s) {

            counts[ch] = counts.getOrDefault(ch, 0) + 1

        }



        var maxFreq = 0

        var maxFreqChars = 0

        for (count in counts.values) {

            if (count > maxFreq) {

                maxFreq = count

                maxFreqChars = 1

            } else if (count == maxFreq) {

                maxFreqChars++

            }

        }



        if ((s.length - maxFreqChars) < (maxFreq - 1) * (k - 1)) {

            return ""

        }



        val heap = PriorityQueue<Triple<Int, Char, Int>>(

            compareBy<Triple<Int, Char, Int>> { it.first }.thenBy { it.second.code },

        )

        for ((ch, count) in counts) {

            heap.offer(Triple(-count, ch, 0))

        }



        val queue = ArrayDeque<Triple<Int, Char, Int>>()

        val result = StringBuilder()

        var index = 0



        while (heap.isNotEmpty() || queue.isNotEmpty()) {

            while (queue.isNotEmpty() && queue.first().third <= index) {

                val item = queue.removeFirst()

                heap.offer(Triple(item.first, item.second, 0))

            }



            if (heap.isEmpty()) {

                return ""

            }



            val (count, ch, _) = heap.poll()

            result.append(ch)

            if (count + 1 < 0) {

                queue.addLast(Triple(count + 1, ch, index + k))

            }

            index++

        }



        return result.toString()

    }

}
