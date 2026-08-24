// LeetCode 1772 - Sort Features by Popularity
// https://leetcode.com/problems/sort-features-by-popularity/

class Solution {
    fun sortFeatures(features: Array<String>, responses: Array<String>): Array<String> {
        val featureSet = features.toHashSet()
        val count = HashMap<String, Int>()
        for (response in responses) {
            val seen = HashSet<String>()
            for (word in response.split(Regex("\\s+"))) {
                if (word in featureSet) {
                    seen.add(word)
                }
            }
            for (word in seen) {
                count[word] = (count[word] ?: 0) + 1
            }
        }
        return features.sortedWith(
            compareByDescending<String> { count[it] ?: 0 }.thenBy { it }
        ).toTypedArray()
    }
}
