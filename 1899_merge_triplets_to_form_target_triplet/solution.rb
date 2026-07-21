# LeetCode 1899 - Merge Triplets to Form Target Triplet
# https://leetcode.com/problems/merge-triplets-to-form-target-triplet/

# @param {Integer[][]} triplets
# @param {Integer[]} target
# @return {Boolean}
def merge_triplets(triplets, target)
  merged = [0, 0, 0]
  triplets.each do |a, b, c|
    if a <= target[0] && b <= target[1] && c <= target[2]
      merged[0] = [merged[0], a].max
      merged[1] = [merged[1], b].max
      merged[2] = [merged[2], c].max
    end
  end
  merged == target
end
