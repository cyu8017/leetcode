// LeetCode 0316 - Remove Duplicate Letters

// https://leetcode.com/problems/remove-duplicate-letters/



class Solution {

    fun removeDuplicateLetters(s: String): String {

        val lastIndex = IntArray(26)

        for (index in s.indices) {

            lastIndex[s[index] - 'a'] = index

        }



        val stack = ArrayDeque<Char>()

        val seen = mutableSetOf<Char>()

        for (index in s.indices) {

            val ch = s[index]

            if (ch in seen) {

                continue

            }

            while (stack.isNotEmpty() && stack.last() > ch && lastIndex[stack.last() - 'a'] > index) {

                seen.remove(stack.removeLast())

            }

            stack.addLast(ch)

            seen.add(ch)

        }

        return stack.joinToString("")

    }

}

