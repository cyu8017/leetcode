# LeetCode 1258 - Synonymous Sentences
# https://leetcode.com/problems/synonymous-sentences/

# @param {String[][]} synonyms
# @param {String} text
# @return {String[]}
def generate_sentences(synonyms, text)
  parent = {}
  find = nil
  find = lambda do |x|
    parent[x] ||= x
    parent[x] = find.call(parent[x]) if parent[x] != x
    parent[x]
  end
  synonyms.each do |a, b|
    ra = find.call(a)
    rb = find.call(b)
    parent[ra] = rb
  end
  groups = Hash.new { |h, k| h[k] = [] }
  parent.keys.each { |word| groups[find.call(word)] << word }
  choices = text.split.map { |w| parent.key?(w) ? groups[find.call(w)].sort : [w] }
  result = [""]
  choices.each do |opts|
    result = result.product(opts).map { |a, b| a.empty? ? b : "#{a} #{b}" }
  end
  result
end
