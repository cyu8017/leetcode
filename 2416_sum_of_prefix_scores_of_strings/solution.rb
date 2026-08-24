# LeetCode 2416 - Sum of Prefix Scores of Strings
# https://leetcode.com/problems/sum-of-prefix-scores-of-strings/

# @param {String[]} words
# @return {Integer[]}
def sum_prefix_scores(words)
  root = { "child" => Array.new(26), "cnt" => 0 }
  words.each do |w|
    cur = root
    w.each_byte do |b|
      c = b - 97
      cur["child"][c] = { "child" => Array.new(26), "cnt" => 0 } if cur["child"][c].nil?
      cur = cur["child"][c]
      cur["cnt"] += 1
    end
  end
  ans = Array.new(words.length, 0)
  words.each_with_index do |w, i|
    cur = root
    s = 0
    w.each_byte do |b|
      cur = cur["child"][b - 97]
      s += cur["cnt"]
    end
    ans[i] = s
  end
  ans
end
