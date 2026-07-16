// LeetCode 0318 - Maximum Product of Word Lengths

// https://leetcode.com/problems/maximum-product-of-word-lengths/



class Solution {

    fun maxProduct(words: Array<String>): Int {

        val count = words.size

        val masks = IntArray(count)

        val lengths = IntArray(count)

        for (index in 0 until count) {

            val word = words[index]

            var mask = 0

            var valid = true

            for (charIndex in word.indices) {

                val bit = 1 shl (word[charIndex] - 'a')

                if (mask and bit != 0) {

                    valid = false

                    break

                }

                mask = mask or bit

            }

            masks[index] = if (valid) mask else 0

            lengths[index] = word.length

        }



        var best = 0

        for (left in 0 until count) {

            if (masks[left] == 0) {

                continue

            }

            for (right in left + 1 until count) {

                if (masks[right] == 0) {

                    continue

                }

                if (masks[left] and masks[right] == 0) {

                    best = maxOf(best, lengths[left] * lengths[right])

                }

            }

        }

        return best

    }

}

