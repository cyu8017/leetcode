# LeetCode 0832 - Flipping an Image
# https://leetcode.com/problems/flipping-an-image/

# @param {Integer[][]} image
# @return {Integer[][]}
def flip_and_invert_image(image)
  image.map { |row| row.reverse.map { |x| 1 - x } }
end
