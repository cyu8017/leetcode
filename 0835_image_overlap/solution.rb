# LeetCode 0835 - Image Overlap
# https://leetcode.com/problems/image-overlap/

# @param {Integer[][]} img1
# @param {Integer[][]} img2
# @return {Integer}
def largest_overlap(img1, img2)
  n = img1.length
  ones1 = []
  ones2 = []
  n.times do |i|
    n.times do |j|
      ones1 << [i, j] if img1[i][j] != 0
      ones2 << [i, j] if img2[i][j] != 0
    end
  end
  return 0 if ones1.empty? || ones2.empty?

  shifts = Hash.new(0)
  ones1.each do |x1, y1|
    ones2.each { |x2, y2| shifts[[x1 - x2, y1 - y2]] += 1 }
  end
  shifts.values.max
end
