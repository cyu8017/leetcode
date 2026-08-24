# LeetCode 0734 - Sentence Similarity
# https://leetcode.com/problems/sentence-similarity/

# @param {String[]} sentence1
# @param {String[]} sentence2
# @param {String[][]} similar_pairs
# @return {Boolean}
def are_sentences_similar(sentence1, sentence2, similar_pairs)
  return false if sentence1.length != sentence2.length

  pairs = {}
  similar_pairs.each do |a, b|
    pairs[[a, b]] = true
    pairs[[b, a]] = true
  end
  sentence1.zip(sentence2).each do |left, right|
    return false if left != right && !pairs[[left, right]]
  end
  true
end
