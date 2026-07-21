# LeetCode 1889 - Minimum Space Wasted From Packaging
# https://leetcode.com/problems/minimum-space-wasted-from-packaging/

# @param {Integer[]} packages
# @param {Integer[][]} boxes
# @return {Integer}
def min_wasted_space(packages, boxes)
  packages = packages.sort
  prefix = []
  packages.each_with_index do |pkg, i|
    prefix << (i == 0 ? pkg : prefix[-1] + pkg)
  end
  answer = Float::INFINITY

  boxes.each do |supplier|
    supplier = supplier.sort
    start = 0
    wasted = 0

    supplier.each do |box|
      # bisect_right packages for box, lo=start
      lo = start
      hi = packages.length
      while lo < hi
        mid = (lo + hi) / 2
        if packages[mid] <= box
          lo = mid + 1
        else
          hi = mid
        end
      end
      ending = lo
      next if ending == start

      package_sum = prefix[ending - 1] - (start > 0 ? prefix[start - 1] : 0)
      wasted += box * (ending - start) - package_sum
      start = ending
    end

    answer = [answer, wasted].min if start == packages.length
  end

  answer == Float::INFINITY ? -1 : answer % 1_000_000_007
end
