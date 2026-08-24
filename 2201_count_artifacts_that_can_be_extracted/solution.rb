# LeetCode 2201 - Count Artifacts That Can Be Extracted
# https://leetcode.com/problems/count-artifacts-that-can-be-extracted/

# @param {Integer} n
# @param {Integer[][]} artifacts
# @param {Integer[][]} dig
# @return {Integer}
def dig_artifacts(n, artifacts, dig)
  dug = {}
  dig.each { |d| dug["#{d[0]},#{d[1]}"] = true }
  ans = 0
  artifacts.each do |a|
    ok = true
    r = a[0]
    while r <= a[2] && ok
      (a[1]..a[3]).each do |c|
        unless dug["#{r},#{c}"]
          ok = false
          break
        end
      end
      r += 1
    end
    ans += 1 if ok
  end
  ans
end
