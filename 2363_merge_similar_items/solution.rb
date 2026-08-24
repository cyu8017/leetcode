# LeetCode 2363 - Merge Similar Items
# https://leetcode.com/problems/merge-similar-items/

# @param {Integer[][]} items1
# @param {Integer[][]} items2
# @return {Integer[][]}
def merge_similar_items(items1, items2)
  mp = Hash.new(0)
  items1.each { |it| mp[it[0]] += it[1] }
  items2.each { |it| mp[it[0]] += it[1] }
  mp.keys.sort.map { |k| [k, mp[k]] }
end
