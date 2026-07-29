# LeetCode 1002 - Find Common Characters
# https://leetcode.com/problems/find-common-characters/

# @param {String[]} words
# @return {String[]}
def common_chars(words)
  common = Hash.new(0)
  words[0].each_char { |ch| common[ch] += 1 }
  words[1..].each do |w|
    cnt = Hash.new(0)
    w.each_char { |ch| cnt[ch] += 1 }
    common.keys.each do |ch|
      common[ch] = [common[ch], cnt[ch]].min
      common.delete(ch) if common[ch] <= 0
    end
  end
  result = []
  common.each { |ch, c| c.times { result << ch } }
  result
end
