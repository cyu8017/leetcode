# LeetCode 0737 - Sentence Similarity II
# https://leetcode.com/problems/sentence-similarity-ii/

# @param {String[]} sentence1
# @param {String[]} sentence2
# @param {String[][]} similar_pairs
# @return {Boolean}
def are_sentences_similar_two(sentence1, sentence2, similar_pairs)
  return false if sentence1.length != sentence2.length

  parent = {}
  find = lambda do |x|
    parent[x] = x unless parent.key?(x)
    while parent[x] != x
      parent[x] = parent[parent[x]]
      x = parent[x]
    end
    x
  end
  union = lambda { |a, b| parent[find.call(a)] = find.call(b) }
  similar_pairs.each { |a, b| union.call(a, b) }
  sentence1.zip(sentence2).none? { |left, right| find.call(left) != find.call(right) }
end
